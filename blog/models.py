# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import template
# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now=True)

    # class Meta:
    #     unique_together = (('name', 'email'),)

    def __str__(self):
        return self.name + " : " + self.email


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author)

    # class Meta:
    #     verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post_by_category', args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author)

    # class Meta:
    #     verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post_by_tag', args=[self.slug])


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="Slug will be generated automatically from the title of the post")
    content = RichTextUploadingField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

    # class Meta:
    #     verbose_plural_name = "PostModel"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
      return reverse('post_detail', args=[self.id])
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)