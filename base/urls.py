from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name ='home'),
    path('uslugi', uslugi, name ='uslugi'),
    path('price', price, name ='price'),
    path('contacts', contacts, name ='contacts'),
    path('about', about, name ='about'),
    path('thanks', thanks, name = 'thanks'),
]