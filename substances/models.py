from django.db import models

# Create your models here.


class Compoundaliases(models.Model):
    """ getting data from the compoundaliases table"""
    id = models.AutoField(primary_key=True)
    modelseedid = models.CharField(max_length=16, null=True)
    externalid = models.CharField(max_length=256, null=True)
    source = models.CharField(max_length=64, null=True)
    comments = models.CharField(max_length=256, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'compoundaliases'

