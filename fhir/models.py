# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Medicationstatement(models.Model):
    concept = models.TextField()
    patientid = models.TextField(db_column='patientId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicationStatement'


class Observation(models.Model):
    coding = models.TextField()
    value = models.FloatField()
    unit = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    patientidentifier = models.TextField(db_column='patientIdentifier', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'observation'


class Patient(models.Model):
    identifier = models.TextField()
    name = models.TextField()
    gender = models.TextField()
    birthdate = models.TextField(db_column='birthDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'