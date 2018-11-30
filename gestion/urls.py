from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contrats/", views.contracts, name="contracts"),
    path("clients/", views.customers, name="customers"),
    path("appartements/", views.apartments, name="apartments"),
]