from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Comment, Post
from .forms import Postform, UpdatePostform, CommentForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


#def home(request):
   # return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    #The request.post stands for filling a form and submitting,
    #then we want to grab d name of the post 4m(as defined in our article_details template, 
    #name="post_id") that form as we're submiting so u attach the .get(), then it bcomes 
    #request.POST.get('post_id')
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
        #To remove a like after liking when u click the like button twice
    else:
        post.likes.add(request.user)#the request.user cos the like was generated 4m a user
        liked = True
        #To add a like
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
 


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #cats = Category.objects.all()
    ordering = ['-post_date']
    #ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
        #This view list all the categories in a dropdown view on any page applied in navbar.


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})
    #This one lists the categories on a dropdown in a single page

def CategoryView(request, cats):
    #The cats is the argument from the url, a variable to hold str
    category_posts = Post.objects.filter(category=cats.title().replace('-', ' '))
    #what the replace function does is to take two argument, what it wants to replace
    #And what will be used for replacement. The above was done to easily slugify(add a dash)
    #to the url since spaces are not allowed in the URL's. Slugify was done in template.
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})
    #We want 2 make sure categories in Post model=category model, then slugify.



class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    #Copied from HomeView and pasted here to allow our drop down for categories to work on this view
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()#we call the fn in our Post model

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True#Pass this as context for us on template

        #As many context as possible can be passed for template use
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes#We can then access this from our article-detail template when we call
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = Postform
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'title_tag', 'author', 'body')

class AddCommentView(CreateView):
    model = Comment
    ordering = ['-date_added']#Look for the time-based one
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    #Let's setup a code that allows our project to figure out which
    #user is filling out the form
    def form_valid(self, form):
        #Let's associate the post id with the comment so that we can 
        #determine the post which will be commented on
        form.instance.post_id = self.kwargs['pk']
        #self.kwargs['pk'] primary key of the post is gotten from the 
        #url /<int:pk>/ of the post which is then passed to form.instance.post_id
        #This will auto-populate our post field and u don't have to select which 
        #post u will be commenting on
        return super().form_valid(form) 

class AddCategoryView(CreateView):
    model = Category
    #form_class = Postform
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'title_tag', 'author', 'body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostform
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostview(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    #If you use a success url, you have to use reverse_lazy, if you're
    #reversing in a function, u have to use reverse.
    #Also, note that reverse() returns a string, hence must be used with args
    #while reverse_lazy() returns an <object>