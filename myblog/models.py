from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
#Make a change to our model to start using ckeditor just installed, also add to settings
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.pk)))
        return reverse('home')    


class Profile(models.Model):
    #We associate this model with our user model with a one-to-one association
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #We have some users that're not already set up, hence the null=True
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
 
    def __str__(self):
        return str(self.user) 
        #This is to make a part of this model visible on the admin
        #Also, u wrap it around the str() cos it's more of an object

    def get_absolute_url(self):
        return reverse('home')  


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #The image folder will be created automatically if we don't have
    full_path = models.TextField(default='myblog/')
    title_tag = models.CharField(max_length=63)
    meta_keywords = models.CharField(max_length=255, default='new')
    meta_description = models.CharField(max_length=255, default='new')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField(), changed to use ckeditor
    post_date = models.DateField(default=timezone.now)
    #timezone.now is imported form django.utils
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    #The default is used for newly created model fields to allow 
    #assigning default values to old objects.
    likes = models.ManyToManyField(User, related_name='blog_posts')
    slug = models.SlugField(max_length=250, unique_for_date='post_date')
    #The related name is some sort of foreign key where manytomany 
    #association associates the many fields to each other.

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('myblog:article-detail', args=[self.post_date.year,
        #                                       self.post_date.month,
        #                                       self.post_date.day, self.slug])
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    #models.CASCADE means if a blog post is deleted, then all 
    #the comments associated with it gets deleted as well,
    #related_name will allow us reference this model as "comments"
    #later on on the blog post page
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
        #return self.post.title + | + str(self.name)

    #def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.pk)))

    #We commented the get_absolute_url cos we've done a reverse_lazy on the view