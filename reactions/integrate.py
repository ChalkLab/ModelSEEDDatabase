import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django.settings")
django.setup()

from django.db.migrations.recorder import MigrationRecorder
from Django.settings import *
from reactions.models import *


# empty table
CompoundsReactions.objects.all().delete()
rxns = Reactions.objects.filter(comments__isnull=True).values_list('reactionid', 'stoichiometry')
for rxnid, rxn in rxns:
    parts = rxn.split(';')
    for part in parts:
        cr = CompoundsReactions()
        pieces = part.split(':')
        coef = pieces[0]
        if float(coef) > 0:
            cr.role = 'product'
        else:
            cr.role = 'reactant'
        cr.stoichiometry = abs(float(coef))
        cr.compoundid = pieces[1]
        cr.form = pieces[2]
        cr.reactionid = rxnid
        cr.save()
        print("saved " + str(cr.id) + " " + rxnid)
exit()
