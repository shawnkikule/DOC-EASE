from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def About(request):
    # return HttpResponse("<h1>This is the about section</h1>")
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')

