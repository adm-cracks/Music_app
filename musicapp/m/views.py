from django.shortcuts import render
from .models import *

# Create your views here.



def index(re):
    s = lag.objects.all()
    return render(re,'index.html',{'s':s})


def mlist(re):
    n = re.GET['name']
    s= song.objects.filter(lag = n)
    print(s)
    return render(re,'mlist.html',{'s':s})


def mdeta(re):
    n = re.GET['id']
    s= song.objects.get(id = n)
    return render(re,'mdeta.html',{'s':s})