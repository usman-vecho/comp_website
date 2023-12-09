from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name='home'),
    path('services/',services,name='services'),
    path('about-us/',about_us,name='about-us'),
    path('faq/',faq,name='faq'),
    path('blogs/',blogs,name='blogs'),
    path("blogs/<slug>",blog_single,name='blog-complete'),
]
