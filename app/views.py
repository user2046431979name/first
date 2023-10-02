from django.shortcuts import render
from .models import *
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator 
# Create your views here.
def index(request):
    rows = News.objects.all()
    top_views = News.objects.all().order_by("-counter")[:3]
    mini_post = News.objects.all().order_by("-created_at")[:4]
    p = Paginator(rows, 2)

    page_number = 1
    
    
    if request.GET.get('page'):
        page_number = int(request.GET.get('page'))


    next_page = page_number + 1 if (page_number) < len(p.page_range) else 1

    previos_page = page_number - 1 if (page_number - 1) != 0 else page_number
    contex = {
        'rows':p.page(page_number),
        'pages':p.page_range,
        'nextP':next_page,
        'previosP':previos_page,
        'top_views':top_views,
        'mini_post':mini_post
    }


    return render(request,'index.html',contex)



def single(request,id):
    row = News.objects.get(id = id)
    rows = NewsDetails.objects.filter(newsobject_id = id)
    images = NewsImages.objects.filter(newsObject_id = id)

    row.counter += 1
    row.save()
    context={
       'i':row,
       'rows':rows,
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

def paginationTest(request):
    rows = ['einz','zwei','drei','vier','funf']
    p = Paginator(rows, 1)
    
    # Paginator() 
    # функция page() возвращает страницу
    
    page_number = 1
    
    if request.GET.get('page'):
        page_number = int(request.GET.get('page'))
    

    context = {
        'rows':p.page(page_number),
        'pages':p.page_range
    }
    return render(request,'PaginationTest.html',context)