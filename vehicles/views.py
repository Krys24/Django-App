from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _


def testlang(request):

    return HttpResponse(_('Welcome to language translation!'))


def index(request):

    # return base.html passing our populated variables title and cal as parameters
    return render(request, 'base.html')


