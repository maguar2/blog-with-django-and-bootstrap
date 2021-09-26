from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User #Model that keeps track of all the users
from django import forms
from django.forms.models import ModelForm
from myblog.models import Profile

class ProfilePageForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'fb_url', 'twitter_url', 'instagram_url', 'pinterest_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}), 
            #'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'fb_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #'attrs' means attributes and this is how bootstrap/css is embeded into the forms
    
    class meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    #We want to call the class and edit some variables that can't be edited as normal forms
    #for security purposes
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    #Has to inherit UserChange Form to be able to make changes to the interactions of the form
    user_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))    
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    #'attrs' means attributes and this is how bootstrap/css is embedded into the forms
    
    class meta:
        model = User
        fields = [{'username': 'user_name'}, 'first_name', 'last_name', 'email', 'password']


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    #'attrs' means attributes and this is how bootstrap/css is embeded into the forms
    
    class meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
