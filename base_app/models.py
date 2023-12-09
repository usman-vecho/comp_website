from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from resizeimage import resizeimage
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify

# Create your models here.

class Blog_category(models.Model):
    name = models.CharField(max_length = 200)
    keyword = models.CharField(max_length = 300,default='None')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('get-category',kwargs = {'slug':slugify(self.keyword)})

class Blog(models.Model):
    blog_image = models.ImageField(upload_to='images_of_blogs/', default = 'images_of_post/default.jpg')
    blog_category = models.ForeignKey(Blog_category , on_delete = models.CASCADE)
    description_to_send = models.TextField(default='None')
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    title = models.CharField(max_length = 300)
    keyword = models.CharField(max_length = 300)
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)
    headline = models.TextField(default='none')
    content = RichTextField()


    def get_absolute_url(self):
        return reverse('blog-complete',kwargs = {'slug':slugify(self.keyword)})

    def __str__(self):
        return self.title