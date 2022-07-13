# code to take a tsv file and create a model definition in the models.py file
# assumptions:
#     all fields should be strings
#     define type of char field based on longest entry
#     add primary key field commensurate with size of tsv files (rows)
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django.settings")
django.setup()

from django.db.migrations.recorder import MigrationRecorder
from Django.settings import *
from functions import *
from ingestion import models
import subprocess
import importlib

# define variables
filepath = '/Biochemistry/reactions.tsv'
tablename = 'reactions'
delimiter = '\t'
modelname = tablename.lower().replace('_', '').capitalize()
datastore = {}
labels = []

# read file and process (add data to the datastore variable)
fp = open(str(BASE_DIR) + filepath)
content = fp.read()
for line in content.splitlines():
    fields = line.split(delimiter)
    # initialize datastore dictionary
    if not datastore:
        for field in fields:
            label = field.replace(" ", "").lower()
            datastore.update({label: []})  # removes spaces from field names
            labels.append(label)
        continue
    # populate fields
    for idx, value in enumerate(fields):
        datastore[labels[idx]].append(value)

# analyze fields for longest entry
maxlens = []
cnt = 0
for key, values in datastore.items():
    if cnt == 0:
        cnt = len(values)
    maxlen = len(str(max(values, key=len)))
    maxlens.append(maxlen)


# check if table is already in database
filepath = "models.py"
classstr = "class " + modelname + '('
out = subprocess.check_output("python ../manage.py inspectdb", shell=True)
if classstr not in out.decode('utf-8'):  # it's output as a byte string
    print("Adding table to DB")

    # check that model is already in models.py
    if not findclass(filepath, classstr):
        # create model text
        mtext = ['\n\nclass ' + modelname + '(models.Model):\n',
                 '    """ getting data from the ' + tablename + ' table """\n',
                 '    id = models.AutoField(primary_key=True)\n']
        for idx, label in enumerate(labels):
            flen = 0
            if maxlens[idx] < 17:
                flen = 16
            elif maxlens[idx] < 65:
                flen = 64
            elif maxlens[idx] < 257:
                flen = 256
            else:
                flen = 16388
            if flen == 16388:
                mtext.append('    ' + label + ' = models.TextField(default=\'\')\n')
            else:
                mtext.append('    ' + label + ' = models.CharField(max_length=' + str(flen) + ', default=\'\')\n')
        mtext.append('    comments = models.CharField(max_length=256, default=\'\')\n')
        mtext.append('    updated = models.DateTimeField(auto_now=True)\n')
        mtext.append('\n')
        mtext.append('    class Meta:\n')
        mtext.append('        managed = True\n')  # this is important as it authorizes Django to add the database
        mtext.append('        db_table = \'' + tablename + '\'\n')

        # add lines to the ingestion models.py
        mfile = open("../ingestion/models.py", "a")  # append mode
        mfile.writelines(mtext)
        mfile.close()
        mfile = open("../ingestion/models.py", "r")
        print(mfile.read())
        mfile.close()

        # run makemigrations
        subprocess.call(["python", "../manage.py", "makemigrations", "ingestion"], stdout=None)
        print('Class created and migrations made')
    else:
        print('Class already created')
    # run migrate
    out = subprocess.call(["python", "../manage.py", "migrate", "ingestion"], stdout=None)
    if out:  # zero means process ran OK
        print("error running migrate")
        subprocess.call(["python", "../manage.py", "migrate", "ingestion"])
        exit()
else:
    print('DB already created')
    # empty table
    cleartable(tablename)

# add data to table by enumerating through the datastore variable and the lists of values for each field
count = 0
importlib.reload(models)  # needed as the code above adds a new model to the models.py after the initial import
for key, values in datastore.items():
    for idx, v in enumerate(values):
        row = getattr(models, modelname)()
        # fill table
        for field in labels:
            setattr(row, field, datastore[field][idx])
        row.save()
        count += 1
        print(row)
    break
print('Complete: added ' + str(count) + ' rows')

# reset files to the starting state
os.remove('migrations/0001_initial.py')
with open('models.py', 'w') as myfile:
    myfile.write('from django.db import models\n')
myfile.close()

# remove the record of the ingestion app migration (so we can do another file)
MigrationRecorder.Migration.objects.filter(app='ingestion').delete()
exit()
