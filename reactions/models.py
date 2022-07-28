from django.db import models


class Reactions(models.Model):
    reactionid = models.CharField(primary_key=True, max_length=16)
    abbreviation = models.TextField()
    name = models.TextField()
    code = models.TextField()
    stoichiometry = models.TextField()
    is_transport = models.CharField(max_length=16)
    equation = models.TextField()
    definition = models.TextField()
    reversibility = models.CharField(max_length=16)
    direction = models.CharField(max_length=16)
    abstract_reaction = models.CharField(max_length=16)
    pathways = models.TextField()
    aliases = models.TextField()
    ec_numbers = models.TextField()
    deltag = models.CharField(max_length=16)
    deltagerr = models.CharField(max_length=16)
    compound_ids = models.TextField()
    status = models.CharField(max_length=256)
    is_obsolete = models.CharField(max_length=16)
    linked_reaction = models.CharField(max_length=256)
    notes = models.CharField(max_length=64)
    source = models.CharField(max_length=64)
    comments = models.CharField(max_length=256)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reactions'


class CompoundsReactions(models.Model):
    compoundid = models.ForeignKey('Compounds', models.DO_NOTHING, db_column='compoundid', blank=True, null=True)
    reactionid = models.ForeignKey('Reactions', models.DO_NOTHING, db_column='reactionid', blank=True, null=True)
    form = models.PositiveIntegerField(blank=True, null=True)
    role = models.CharField(max_length=8, blank=True, null=True)
    stoichiometry = models.FloatField(blank=True, null=True)
    updated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'compounds_reactions'
        unique_together = (('compoundid', 'reactionid', 'form'),)


class Compounds(models.Model):
    compoundid = models.CharField(primary_key=True, max_length=16)
    abbreviation = models.TextField()
    name = models.TextField()
    formula = models.CharField(max_length=64)
    mass = models.CharField(max_length=16)
    source = models.CharField(max_length=64)
    inchikey = models.CharField(max_length=64)
    charge = models.CharField(max_length=16)
    is_core = models.CharField(max_length=16)
    is_obsolete = models.CharField(max_length=16)
    linked_compound = models.CharField(max_length=64)
    is_cofactor = models.CharField(max_length=16)
    deltag = models.CharField(max_length=16)
    deltagerr = models.CharField(max_length=16)
    pka = models.CharField(max_length=256)
    pkb = models.CharField(max_length=256)
    abstract_compound = models.CharField(max_length=16)
    comprised_of = models.CharField(max_length=16)
    aliases = models.TextField()
    smiles = models.TextField()
    notes = models.CharField(max_length=16)
    comments = models.CharField(max_length=256)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'compounds'


class Identifiers(models.Model):
    cpds = models.ForeignKey('Compounds', models.DO_NOTHING)
    type = models.CharField(max_length=256)
    value = models.TextField()
    source = models.CharField(max_length=64, blank=True, null=True)
    comment = models.CharField(max_length=256, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'identifiers'
