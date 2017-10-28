# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django import template

# Create your views here.

from blog.models import Post, Category, Tag


def post_list(request):
    posts = Post.objects.order_by("-id").all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def get_recent_posts(request, num=3):
    recentPosts = Post.objects.all().order_by('-id')[:num]
    return render(request, 'blog/landpage.html', {'recentPosts': recentPosts})

def tag_list(request):
    tags = Tag.objects.order_by("-id").all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

def category_list(request):
    categories = Category.objects.order_by("-id").all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', context={'post': post})

def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'blog/post_by_tag.html', context )

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')






