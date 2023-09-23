from django.shortcuts import render
from .models import *
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    rows = News.objects.all()
    top_views = News.objects.all().order_by("-counter")[:5]
    
    contex = {
        'rows':rows,
        'top_views':top_views
    }


    return render(request,'index.html',contex)



def single(request,id):
    row = News.objects.get(id = id)
    
    

    row.counter += 1
    row.save()


    images = NewsImages.objects.filter(newsObject_id = id)


    context={
       'i':row,
       'images':images
    }
    return render(request,'single.html',context)
def about(request):
    User = get_user_model() 
    User = User.objects.all()
    img = Gallery.objects.all()
    context ={
        'img':img,
        'users':User
    }
    return render(request,'about.html',context)
def test(request,num):
    return render(request,'1.html',{'num':num,'num2':num**2,'list':[i for i in range(100007)],'name':'name'})
    