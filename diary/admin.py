from django.contrib import admin

from .models import BlogPost

#Djangoの管理サイトにmodelクラスのBlogPostを登録
admin.site.register(BlogPost)

