# Generated by Django 4.2.7 on 2023-11-29 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='логин')),
                ('first_name', models.CharField(max_length=150, verbose_name='имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='фамилия')),
                ('middle_name', models.CharField(max_length=150, verbose_name='отчество')),
                ('is_active', models.BooleanField(default=True, verbose_name='активный')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='администратор')),
                ('is_staff', models.BooleanField(default=False, verbose_name='штатный сотрудник')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='изменен')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.department', verbose_name='подразделение')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
                'ordering': ('-created_at',),
            },
        ),
    ]