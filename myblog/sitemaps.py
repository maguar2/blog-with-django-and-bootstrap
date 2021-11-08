from django.contrib.sitemaps import Sitemap

from .models import Post

#class Static_Sitemap(Sitemap):
#    """Aids google crawlers in crawling your site when indexed properly"""
#    priority = 1.0
#    changefreq = 'yearly'

#    def items(self):
#        return ['home', 'category']

#    def location(self, item):
#        return reverse(item)


class Post_Sitemap(Sitemap):
    priority = 0.7
    changefreq = "daily"

    def items(self):
        """Where we will query the db for what we want and make it globally accessible as obj"""
        return Post.objects.all()
        #This will be available for the whole of class as obj

    def location(self, obj):
        """Queries the location in the returned obj from items"""
        return obj.full_path

    def lastmod(self, obj):
        """returns the datetime of when it was last modified"""
        return obj.post_date