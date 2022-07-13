""" urls for the reactions app """
from django.urls import path
from compounds import views


urlpatterns = [
    path("view/<cmpid>", views.view, name='view'),
]
