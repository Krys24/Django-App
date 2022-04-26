from django.urls import path
from vehicles.views import *

urlpatterns = [
    path('', index, name='index')
]
