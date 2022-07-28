# import operator.or
from scidatalib.scidata import SciData
import json
import pandas as pd
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django.settings")
django.setup()
from reactions.models import *
from django.db.models import Q

rxnid = 'rxn00001'
example = SciData(rxnid)

rxn = Reactions.objects.filter(reactionid='rxn00001').values()
cmpnts = CompoundsReactions.objects.filter(reactionid=rxnid).values()
cpds = []
ali = []
test = 0
for cpt in cmpnts:
    ### SELECT * FROM `identifiers_test_mm` where cpds_id = 'cpd00001' and (type = 'casrn' or type = 'inchikey' or type = 'iupacname' or type = 'csmiles');
    # list = [Q(type='inchikey') | Q(type='casrn') | Q(type='pubchemid') | Q(type='csmiles') | Q(type='iupacname')]
    # cpdid = Identifiers.objects.filter(reduce(list, cpds_id=cpt['compoundid_id']))
    # cpdid = Identifiers.objects.filter("SELECT * FROM `identifiers_test_mm` where cpds_id = 'cpd00001' and (type = 'casrn' or type = 'inchikey' or type = 'iupacname' or type = 'csmiles')")
    # cpdid = Identifiers.objects.filter((Q(type='inchikey') | Q(type='casrn') | Q(type='pubchemid') | Q(type='csmiles') | Q(type='iupacname')).filter(cpds_id=cpt['compoundid_id'])).values()
    # cpdid = Identifiers.objects.filter((Q(type='casrn') | Q(type='inchikey') | Q(type='pubchemid') | Q(type='csmiles') | Q(type='iupacname')) & Q(cpds_id=cpt['compoundid_id'])).values()
    # print(cpdid)
    for ide in cpdid:
        iden = {
            '@id': 'identifier',
            'type': ide['type'],
            'value': ide['value'],
            'source': ide['source']
        }
        ali.append(iden)
#     comp = {
#         '@id': 'compound',
#         'cpdid': cpt['compoundid_id'],
#         'form': cpt['form'],
#         'role': cpt['role'],
#         'stoichiometry': cpt['stoichiometry'],
#         'aliases': ali[test]
#     }
#     test += 1
#     cpds.append(comp)
# facets = [cpds]
# for facet in facets:
#     example.facets(facet)
# print(json.dumps(example.output, indent=4, ensure_ascii=False))
# print(cpdid)
# print(ali)

