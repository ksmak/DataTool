from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.exceptions import ValidationError
from metadata.models import Department, Database, Form


class MyUserManager(BaseUserManager):
    """MyUser manager"""

    def create_user(
        self,
        username: str,
        password: str
    ) -> 'MyUser':

        if not username:
            raise ValidationError('Username required')

        client: 'MyUser' = self.model(
            username=username
        )
        client.set_password(password)
        client.save(using=self._db)
        return client

    def create_superuser(
        self,
        username: str,
        password: str
    ) -> 'MyUser':

        client: 'MyUser' = self.model(
            username=username
        )
        client.is_staff = True
        client.is_superuser = True
        client.set_password(password)
        client.save(using=self._db)
        return client


class MyUser(AbstractBaseUser, PermissionsMixin):
    """MyUser model"""

    username = models.CharField(
        verbose_name='логин',
        max_length=50,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=150
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=150
    )
    middle_name = models.CharField(
        verbose_name='отчество',
        max_length=150
    )
    department = models.ForeignKey(
        verbose_name='подразделение',
        to=Department,
        on_delete=models.RESTRICT,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name='активный',
        default=True
    )
    is_superuser = models.BooleanField(
        verbose_name='администратор',
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name='штатный сотрудник',
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name='создан',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='изменен',
        auto_now=True
    )

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self) -> str:
        return self.username

    @property
    def full_name(self):
        if self.last_name or self.first_name:
            return f"{self.last_name} {self.first_name}".strip()
        else:
            return self.username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = (
            '-created_at',
        )


class Role(models.Model):
    """Role model"""

    name = models.CharField(
        verbose_name='наименование',
        max_length=150
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'роль'
        verbose_name_plural = 'роли'
        ordering = (
            'name',
        )


class UserRole(models.Model):
    """UserRole model"""

    user = models.ForeignKey(
        verbose_name='пользователь',
        to=MyUser,
        on_delete=models.RESTRICT
    )

    role = models.ForeignKey(
        verbose_name='роль',
        to=Role,
        on_delete=models.RESTRICT
    )

    def __str__(self) -> str:
        return f"{self.user} {self.role}"

    class Meta:
        verbose_name = 'роли пользователя'
        verbose_name_plural = 'роли пользователей'
        ordering = (
            'user',
            'role',
        )


class DatabaseAccess(models.Model):
    """Database access model"""

    role = models.ForeignKey(
        verbose_name='роль',
        to=Role,
        on_delete=models.RESTRICT
    )

    database = models.ForeignKey(
        verbose_name='база данных',
        to=Database,
        on_delete=models.RESTRICT
    )

    def __str__(self) -> str:
        return f"{self.role} {self.database}"

    class Meta:
        verbose_name = 'доступ к БД'
        verbose_name_plural = 'доступ к БД'
        ordering = (
            'role',
        )


class FormAccess(models.Model):
    """Form access model"""

    INPUT_FORM_ACCESS_TYPE = [
        ('read', 'чтение'),
        ('write', 'запись'),
        ('delete', 'удаление'),
    ]

    role = models.ForeignKey(
        verbose_name='роль',
        to=Role,
        on_delete=models.RESTRICT
    )

    form = models.ForeignKey(
        verbose_name='форма',
        to=Form,
        on_delete=models.RESTRICT
    )

    access_type = models.CharField(
        verbose_name='тип доступа',
        max_length=10,
        choices=INPUT_FORM_ACCESS_TYPE,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.role} {self.form}"

    class Meta:
        verbose_name = 'доступ к формам'
        verbose_name_plural = 'доступ к формам'
        ordering = (
            'role',
        )
