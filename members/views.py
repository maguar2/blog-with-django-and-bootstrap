from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from myblog.models import Profile
#Import the view below to change django stock template

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"
    #fields = '__all__'

    #Let's setup a code that allows our project to figure out which
    #user is filling out the form
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'fb_url', 'twitter_url', 'instagram_url', 'pinterest_url']
    #The fields above are those of Profile extended from the User Model to add more functionalities
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile 
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        #Let's get the pk(Primary Key) of the user currently using the page and return as context        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])        
        
        context["page_user"] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    #success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    #Lets make our user profile know the current logged in user for profile editing purpose
    def get_object(self):
        return self.request.user
    


