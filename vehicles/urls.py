from django.urls import path
from vehicles.views import *

app_name = 'vehicles'
urlpatterns = [
    path('testlang', testlang, name='testlang'),
    path('', index, name='index'),
]

