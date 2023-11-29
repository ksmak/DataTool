from django.db import models


class Department(models.Model):
    """Department model"""

    title = models.CharField(
        verbose_name='наименование',
        max_length=200,
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'подразделение',
        verbose_name_plural = 'подразделения'


class Dictionary(models.Model):
    """Dictionary model"""

    title = models.CharField(
        verbose_name='наименование',
        max_length=200
    )

    table_name = models.CharField(
        verbose_name='имя таблицы',
        max_length=50
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'справочник',
        verbose_name_plural = 'справочники'


class Database(models.Model):
    """Database model"""

    order = models.PositiveSmallIntegerField(
        verbose_name='порядковый номер',
        default=0
    )

    title = models.CharField(
        verbose_name='наименование',
        max_length=200
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'база данных',
        verbose_name_plural = 'базы данных'
        ordering = (
            '-order',
        )


class Form(models.Model):
    """Form model"""

    FORM_TYPE = [
        ('input_form', 'Форма для ввода информации'),
        ('search_form', 'Форма для поиска информации'),
    ]

    order = models.PositiveSmallIntegerField(
        verbose_name='порядковый номер',
        default=0
    )

    title = models.CharField(
        verbose_name='наименование',
        max_length=200
    )

    db = models.ForeignKey(
        verbose_name='база данных',
        to=Database,
        on_delete=models.RESTRICT,
        related_name='forms'
    )

    form_type = models.CharField(
        verbose_name='тип формы',
        max_length=15,
        choices=FORM_TYPE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'форма',
        verbose_name_plural = 'формы'
        ordering = (
            '-order',
        )


class Group(models.Model):
    """Group model"""

    order = models.PositiveSmallIntegerField(
        verbose_name='порядковый номер',
        default=0
    )

    title = models.CharField(
        verbose_name='наименование',
        max_length=200
    )

    form = models.ForeignKey(
        verbose_name='форма',
        to=Form,
        on_delete=models.RESTRICT,
        related_name='groups'
    )

    is_multy = models.BooleanField(
        verbose_name='мультигруппа',
        default=False
    )

    table_name = models.CharField(
        verbose_name='имя таблицы',
        max_length=50
    )

    def __str__(self):
        return f'{self.form.title}: {self.title}'

    class Meta:
        verbose_name = 'группа',
        verbose_name_plural = 'группы'
        ordering = (
            '-order',
        )


class Field(models.Model):
    """Field model"""

    FIELD_TYPE = [
        ('text', 'Простой текст без ограничений'),
        ('number', 'Целое число'),
        ('cyrillic', 'Только кириллица'),
        ('dict', 'Справочное значение'),
    ]

    order = models.PositiveSmallIntegerField(
        verbose_name='порядковый номер',
        default=0
    )

    title = models.CharField(
        verbose_name='наименование',
        max_length=200
    )

    group = models.ForeignKey(
        verbose_name='группа',
        to=Group,
        on_delete=models.RESTRICT,
        related_name='fields'
    )

    field_name = models.CharField(
        verbose_name='имя поля',
        max_length=50
    )

    field_type = models.CharField(
        verbose_name='тип поля',
        max_length=15,
        choices=FIELD_TYPE
    )

    len = models.PositiveIntegerField(
        verbose_name='длина',
        default=0
    )

    is_key = models.BooleanField(
        verbose_name='ключевое поле',
        default=False
    )

    is_visible = models.BooleanField(
        verbose_name='видимость',
        default=False
    )

    is_enable = models.BooleanField(
        verbose_name='доступен',
        default=False
    )

    is_require = models.BooleanField(
        verbose_name='обязательный ввод',
        default=False
    )

    precision = models.PositiveIntegerField(
        verbose_name='точность',
        default=0
    )

    is_duplicate = models.BooleanField(
        verbose_name='создать дубликат',
        default=False
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'поле',
        verbose_name_plural = 'поля'
        ordering = (
            '-order',
        )


class Report(models.Model):
    """Report model"""

    order = models.PositiveSmallIntegerField(
        verbose_name='порядковый номер',
        default=0
    )

    title = models.CharField(
        verbose_name='наименование',
        max_length=200
    )

    template = models.FileField(
        verbose_name='шаблон',
        upload_to='templates/',
        null=True,
        blank=True
    )

    data = models.JSONField(
        verbose_name='json',
        null=True,
        blank=True
    )

    db = models.ForeignKey(
        verbose_name='база данных',
        to=Database,
        on_delete=models.RESTRICT,
        related_name='reports'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'отчет',
        verbose_name_plural = 'отчеты'
        ordering = (
            '-order',
        )


class Converter(models.Model):
    """Converter model"""

    order = models.PositiveSmallIntegerField(
        verbose_name='порядковый номер',
        default=0
    )

    title = models.CharField(
        verbose_name='наименование',
        max_length=200
    )

    form = models.OneToOneField(
        verbose_name='форма',
        to=Form,
        on_delete=models.RESTRICT
    )

    data = models.JSONField(
        verbose_name='json',
        null=True,
        blank=True
    )

    db = models.ForeignKey(
        verbose_name='база данных',
        to=Database,
        on_delete=models.RESTRICT,
        related_name='converters'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'конвертор',
        verbose_name_plural = 'конверторы'
        ordering = (
            '-order',
        )
