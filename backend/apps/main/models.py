# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Documents(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_active = models.BooleanField()
    old_id = models.BigIntegerField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_user = models.CharField(max_length=150)
    changed_at = models.DateTimeField()
    changed_user = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'documents'


class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    is_enable = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'countries'


class Nationals(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    is_enable = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'nationals'


class Registrationstate(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    is_enable = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'registrationstate'


class Asb(models.Model):
    id = models.BigAutoField(primary_key=True)
    doc = models.ForeignKey(Documents, models.DO_NOTHING, blank=True, null=True)
    lst = models.SmallIntegerField()
    surname = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    iin = models.BigIntegerField(blank=True, null=True)
    citizen = models.BigIntegerField(blank=True, null=True)
    nation = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asb'


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    doc = models.ForeignKey(Documents, models.DO_NOTHING, blank=True, null=True)
    lst = models.SmallIntegerField()
    region = models.CharField(max_length=150, blank=True, null=True)
    district = models.CharField(max_length=150, blank=True, null=True)
    punkt = models.CharField(max_length=150, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'address'
