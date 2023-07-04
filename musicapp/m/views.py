from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
import random
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


def play(re):
    data= song.objects.all()
    page = Paginator(data,1)
    page_list = re.GET.get('page')
    page=page.get_page(page_list)
    col = ['#C38EB4','3E1CBD7','#86ABCF','#26425A','#6DA5CO','#F1916D']
    c=random.choice(col)
    print(c)
    return render(re,'play.html',{'page':page,'col':c})