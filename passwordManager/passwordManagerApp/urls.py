from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.site_list, name="sites"),

]
