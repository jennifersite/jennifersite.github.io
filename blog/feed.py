from django.contrib.syndication.views import Feed
from blog.models import Post
from django.conf import settings
from django.utils.feedgenerator import Rss201rev2Feed
from blog.templatetags import custom_markdown
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from blog.models import Author


class DjangoBlogFeed(Feed):
    feed_type = Rss201rev2Feed

    description = 'Updates on new comments on Dreamreal entry.'
    feed_url = 'https:127.0.0.1:8000/feed'
    title = "%s %s " % ("Jennifer's Blog", 'Updates on new comments on Dreamreal entry.')
    link = "https:127.0.0.1:8000"

    def author_name(self):
        return Author.name

    def items(self):
        return Post.objects.order_by('-pk')[:5]

    def item_title(self, item):
        return item.title

    def feed_copyright(self):
        # print(Site.objects.get_current().name)
        return "Copyright 2017  " + "Jennifer's Blog"

    def item_link(self, item):
        return item.get_absolute_url()
