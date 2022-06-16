# code to take a tsv file and create a model definition in the models.py file
# assumptions:
#     all fields should be strings
#     define type of char field based on longest entry
#     add primary key field commensurate with size of tsv files (rows)
from Django.settings import *

filename = 'Unique_ModelSEED_Compound_Aliases.tsv'
tablename = 'compoundaliases'

fp = open(str(BASE_DIR) + '/Biochemistry/Aliases/' + filename)
content = fp.read()
datastore = {}
for line in content.splitlines():
    fields = line.split('\t')
    # initialize datastore dictionary
    if not datastore:
        labels = []
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

# create model text
mtext = ['\nclass ' + tablename.lower().capitalize() + '(models.Model):\n',
         '    """ getting data from the ' + tablename.lower() + ' table """\n',
         '    id = models.AutoField(primary_key=True)\n']
for idx, label in enumerate(labels):
    flen = 0
    if maxlens[idx] < 17:
        flen = 16
    elif maxlens[idx] < 65:
        flen = 64
    elif maxlens[idx] < 257:
        flen = 256
    elif maxlens[idx] < 1025:
        flen = 1025
    else:
        flen = 4096
    mtext.append('\t' + label + ' = models.CharField(max_length=' + str(flen) + ', default=\'\')\n')
mtext.append('    comments = models.CharField(max_length=256, null=True)\n')
mtext.append('    updated = models.DateTimeField(auto_now=True)\n')
mtext.append('\n')
mtext.append('    class Meta:\n')
mtext.append('        managed = False\n')
mtext.append('        db_table = \'' + tablename.lower() + '\'\n')
# add lines to models.py
mfile = open("models.py", "a")  # append mode
mfile.writelines(mtext)
mfile.close()
mfile = open("models.py", "r")
print(mfile.read())
mfile.close()

exit()
