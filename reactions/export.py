import os
import django
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django.settings")
django.setup()
from reactions.models import *

rxn = Reactions.objects.filter(reactionid='rxn00001').values()[0]
cmpnts = list(CompoundsReactions.objects.filter(reactionid=rxn['reactionid']).values())
cmpids = []
for cmp in cmpnts:
    cmpids.append(cmp['compoundid_id'])
cmpds = list(Compounds.objects.filter(compoundid__in=cmpids).values())
data = {'reaction': rxn, 'components': cmpnts, 'compounds': cmpds}
print(json.dumps(data, indent=4, default=str))
