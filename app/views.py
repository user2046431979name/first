from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    rows = News.objects.all()
    contex = {
        'rows':rows
    }


    return render(request,'index.html',contex)



def single(request):
    return render(request,'single.html')