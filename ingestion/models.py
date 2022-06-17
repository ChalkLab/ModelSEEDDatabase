from django.db import models


class Reactionaliases(models.Model):
    """ getting data from the reaction_aliases table """
    id = models.AutoField(primary_key=True)
    modelseedid = models.CharField(max_length=16, default='')
    externalid = models.CharField(max_length=64, default='')
    source = models.CharField(max_length=64, default='')
    comments = models.CharField(max_length=256, default='')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'reaction_aliases'
