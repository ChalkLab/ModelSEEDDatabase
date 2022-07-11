""" views for compounds """
from django.shortcuts import render
from django.core.paginator import Paginator
from reactions.models import *


def view(request, cmpid):
    """ view a reaction """
    cmp = Compounds.objects.get(compoundid=cmpid)
    return render(request, "Compounds/view.html", {"cmp": cmp})
