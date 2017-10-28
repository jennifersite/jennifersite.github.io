

from django.conf.urls import url
from django.contrib import admin
from blog.feed import DjangoBlogFeed
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
from blog import views

urlpatterns = [
    url(r'^feed/$',DjangoBlogFeed()),
    url(r'^sitemap\.xml/$', sitemap, {'sitemaps' : sitemap } , name='sitemap'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^tag/$', views.tag_list, name='tag_list'),
    url(r'^category/$', views.category_list, name='category_list'),
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^$', views.get_recent_posts, name='get_recent_posts'),
    url(r'^posts/$', views.post_list, name='post_list'),
]

sitemaps = {
    'posts': PostSitemap
}
