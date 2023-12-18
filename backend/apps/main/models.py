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


class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    is_enable = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'region'


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    doc = models.ForeignKey(Documents, models.DO_NOTHING, blank=True, null=True)
    lst = models.SmallIntegerField()
    punkt = models.CharField(max_length=150, blank=True, null=True)
    raion = models.CharField(max_length=150, blank=True, null=True)
    obl = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'address'


class Asb(models.Model):
    id = models.BigAutoField(primary_key=True)
    doc = models.ForeignKey(Documents, models.DO_NOTHING, blank=True, null=True)
    lst = models.SmallIntegerField()
    obl = models.BigIntegerField(blank=True, null=True)
    dr = models.DateField(blank=True, null=True)
    ot = models.CharField(max_length=50, blank=True, null=True)
    im = models.CharField(max_length=50, blank=True, null=True)
    fam = models.CharField(max_length=50, blank=True, null=True)
    iin = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asb'
