# Generated by Django 2.2 on 2023-07-29 12:47

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('keyword', models.CharField(default='None', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_image', models.ImageField(default='images_of_post/default.jpg', upload_to='images_of_blogs/')),
                ('description_to_send', models.TextField(default='None')),
                ('title', models.CharField(max_length=300)),
                ('keyword', models.CharField(max_length=300)),
                ('tags', models.CharField(default='none', max_length=300)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('headline', models.TextField(default='none')),
                ('content', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.Blog_category')),
            ],
        ),
    ]
