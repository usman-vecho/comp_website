from django.shortcuts import render
from .models import *
from django.shortcuts import render,HttpResponse
#from .models import 
# Create your views here.


def home(request):
    return render(request,'base_app/index-demo-1.html',{})


def services(request):
    return render(request,'base_app/services.html')

def faq(request):
    return render(request,'base_app/faq.html')

def about_us(request):
    return render(request,'base_app/about-us.html',{})
    
def contact_us(request):
    return render(request,'base_app/contact-us.html',{})

#def blogs(request):
#    return render(request,'base_app/index-blog.html',{})


def blogs(request):
    blogs = Blog.objects.all()
    Blog_categories = Blog_category.objects.all()
    return render(request,'base_app/index-blog.html',{'blogs':blogs,'Blog_categories':Blog_categories,})


def blog_single(request,slug):
    slug = slug.replace('-',' ')
    blog_ = Blog.objects.get(keyword=slug)
    targeted_blogs = Blog.objects.all().order_by('?')[:7]
    Blog_categories = Blog_category.objects.all()
    return render(request,'base_app/index-single-blog.html',{'blog_':blog_,'Blog_categories':Blog_categories,'targeted_blogs':targeted_blogs})



