from django.contrib import admin

# Register your models here so that you can CRUD them from Django Admin Site
from web.models import Comment, Article, Topic, Business, Profile

admin.site.register(Article)

admin.site.register(Topic)

admin.site.register(Comment)

admin.site.register(Business)

admin.site.register(Profile)