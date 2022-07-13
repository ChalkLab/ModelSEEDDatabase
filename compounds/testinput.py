import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django.settings")
django.setup()

from django.db.migrations.recorder import MigrationRecorder
from Django.settings import *
from compounds.models import *
from compounds.testfunctions import *
import subprocess
import importlib
import requests

x = 1
print(x)

# compoundsdata = CompoundsMm.objects.all()
# for compound in compoundsdata.iterator():
# for compound in CompoundsMm.objects.all():
#     x = 0
#     ickey = str(CompoundsMm.objects.values_list('inchikey')[x])
#     ichkey = ickey[2]
#     print(ickey)
#     x = x+1
    # text = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/' + ickey + '/property/IUPACname/txt')
    # unfiltered = str(text.content)
    # iupacName = filterText(unfiltered)
    # cpd = CompoundsMm.objects.get(inchikey = ickey)
    # cpd.iupac_name = iupacName
    # cpd.save()

# input for iupac_name -> got to id 12320 before timeout / lost connection, 41 with 503 error
cpdset = CompoundsMm.objects.all()
for cpd in cpdset.iterator():
    ickey = str(cpd.inchikey)
    text = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/' + ickey + '/property/IUPACname/txt')
    unfiltered = str(text.content)
    iupacName = filterText(unfiltered)
    cpd.iupac_name = iupacName
    cpd.save()
    print('Added ' + str(x) + ' rows')
    x = x + 1

#24652 to start, either blank or with 503 error, 11886 blank before resolving 503 (53 errors), 11898 after
# cpdset = CompoundsMm.objects.all()
# for cpd in cpdset.iterator():
#     iup = cpd.iupac_name
#     if('503' in iup):
#         ickey = str(cpd.inchikey)
#         text = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/' + ickey + '/property/IUPACname/txt')
#         unfiltered = str(text.content)
#         iupacName = filterText(unfiltered)
#         cpd.iupac_name = iupacName
#         cpd.save()
#         # print(str(cpd.name))
#         print('Added ' + str(x) + ' rows')
#         x = x + 1

# input for 9739 compounds with no listed inchikey, need to remove 404 errors and replace /n with ;
# cpdset = CompoundsMm.objects.all()
# for cpd in cpdset.iterator():
#     ickey = str(cpd.inchikey)
#     cpdname = str(cpd.name)
#     if(ickey == ""):
#     # if('503' in ickey):
#         text = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/' + cpdname + '/property/InChIKey/txt')
#         unfiltered = str(text.content)
#         inchik = filterSeperateText(unfiltered)
#         # print(inchik)
#         cpd.inchikey = inchik
#         cpd.save()
#         print('Added ' + str(x) + ' rows')
#         x = x + 1

