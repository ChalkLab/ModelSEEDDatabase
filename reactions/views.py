""" views for reactions """
from django.shortcuts import render
from django.core.paginator import Paginator
from reactions.models import *


def home(request):
    """ get the stats on the DB and show the home page """
    cmpcnt = Compounds.objects.all().count()
    rxncnt = Reactions.objects.all().count()
    return render(request, "Reactions/home.html", {'cmpcnt': cmpcnt, 'rxncnt': rxncnt})


def index(request):
    """ get a list of the reactions """
    rxns = Reactions.objects.all().values('name', 'reactionid').order_by('name')

    paginator = Paginator(rxns, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "Reactions/list.html", {"page_obj": page_obj})


def view(request, rxnid):
    """ view a reaction """
    rxn = Reactions.objects.get(reactionid=rxnid)
    return render(request, "Reactions/view.html", {"rxn": rxn})
