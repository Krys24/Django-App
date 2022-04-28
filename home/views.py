from django.shortcuts import render

# This is a function we will set up a path to in our urls.py
def index(request):

# return base.html passing our populated variables title and cal as parameters
    return render(request, 'index.html')
