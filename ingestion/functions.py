""" file of useful functions to support ingestion """
from django.db import connection


def findclass(file=None, strng=None):
    found = False
    if strng is None or file is None:
        return found
    fp = open(file, "r")
    file = fp.read()
    if strng in file:
        found = True
    return found


def cleartable(tablename=None):
    if tablename:
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE " + tablename)
    return

