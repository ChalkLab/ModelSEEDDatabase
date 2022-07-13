import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django.settings")
django.setup()

from django.db.migrations.recorder import MigrationRecorder
from django.db.models import Q
from Django.settings import *
from identifiers.models import *
from compounds.testfunctions import *
import requests
import re

# https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N/property/IUPACname/txt
# https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N/synonyms/txt

#casrns from pubchem
searchablecpds = CompoundsMm.objects.exclude(Q(inchikey='') | Q(inchikey__isnull=True) | Q(inchikey__contains=';')).values_list('compoundid', 'inchikey')
for ids, cpd in searchablecpds:
    # iden = IdentifiersTestMm()
    sucess = False
    while not sucess:
        test = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/' + cpd + '/synonyms/txt')
        text = str(test.content)[2:-3]
        if 'PUGREST.ServerError' in test:
            continue
        else:
            sucess = True
    synonyms = text.split('\\n')
    for syn in synonyms:
        match = re.search('\d{2,7}-\d{2}-\d', syn)
        if match is not None:
            print(syn)
            # iden.cpds_id = ids
            # iden.type = 'casrn'
            # iden.value = syn
            # iden.source = 'pubchem'
            # iden.save()
            print(ids)
            break



# for pubchem
# def findInChIKey:
#
#
# def findIUPAC(list):
#     for inch in list:
#         if

# def findSMILES:
#     requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/' + ickey + '/property/canonicalsmiles/txt')
#
# def findInChI:
#     requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/' + ickey + '/property/inchi/txt')

# searchablecpds = CompoundsMm.objects.exclude(Q(inchikey='') | Q(inchikey__isnull=True) | Q(inchikey__contains=';')).values_list('inchikey')
# print(searchablecpds)
# busy = False
# for cpd in searchablecpds:
#     print(cpd)
#     while not busy:
#         iden = IdentifiersTestMm()

    #     print(cpd)
        # text = (get requests)
        # if text =

# print(y)
# if y == 10:
# x = True
# print(searchablecpds)
