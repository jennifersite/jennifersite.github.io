# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django import forms
from pagedown.widgets import AdminPagedownWidget

from blog import models
from blog.models import Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ['name', 'email']
    ordering = ['-name']
    list_filter = ['active']
    date_hierarchy = 'created_on'


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Post
        fields = '__all__'
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'pub_date', 'author', 'category',)
    search_fields = ['title', 'content']
    ordering = ['-pub_date']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    readonly_fields = ('slug',)
    fields = ('title', 'slug', 'content', 'author', 'category', 'tags',)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tag, TagAdmin)