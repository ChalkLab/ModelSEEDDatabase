""" urls for the reactions app """
from django.urls import path
from reactions import views


urlpatterns = [
    path("", views.home, name='home'),
    path("list/", views.index, name='list'),
    path("view/<rxnid>", views.view, name='view'),
]
