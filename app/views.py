from django.shortcuts import render
from .models import *
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView 

# Create your views here.
def index(request):
    about_images = Gallery.objects.all()[:5]
    is_admin = False

    if request.user.is_authenticated:
        try:
            role = Admins.objects.get(selectedUser=request.user)
            is_admin = True
        except:
            pass
    query = ""
   
    rows = News.objects.all()
    if request.GET.get('query'):
        query = request.GET.get('query')
        rows = News.objects.all().filter(title__icontains = query)
    
    
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
        'mini_post':mini_post,
        'is_admin':is_admin,
        'about_images':about_images
    }


    return render(request,'index.html',contex)
def likes(request):
    id = request.GET.get('id')
    row = News.objects.get(id = id)
    row.like_count += 1
    row.save()
    return index(request)



   


def single(request,id):
    row = News.objects.get(id = id)
    rows = NewsDetails.objects.filter(newsobject_id = id)
    images = NewsImages.objects.filter(newsObject_id = id)

    comm = Comments.objects.filter(newsObject_id = id)

    row.counter += 1
    row.save()
    context={
       'i':row,
       'rows':rows,
       'images':images,
       'comm':comm
    }
    return render(request,'single.html',context)
def comments(request,id):
    
    name = request.POST.get('name')
    text = request.POST.get('text')
    row = News.objects.get(id=id)
    Comments.objects.create(newsObject=row, name = name , text = text)
    return single(request,id)
def about(request):
    User = get_user_model() 
    User = User.objects.all()
    img = Gallery.objects.all()
    context ={
        'img':img,
        'users':User
    }
    return render(request,'about.html',context)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"








































"""
def search(request):
    #query
    
    l = [i for i in range(10000)]
    query = request.GET.get('query')
    if query == None:
        rows = News.objects.filter(title__icontains='first_title')
    else:
        rows = News.objects.filter(title__icontains=query)
    context = {
        'rows':rows,
        'l':l,

    }
    return render(request,'Search.html',context)
"""