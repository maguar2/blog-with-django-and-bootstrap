from django.urls import path
from .views import ShowProfilePageView, UserRegisterView, UserEditView, PasswordsChangeView, EditProfilePageView, CreateProfilePageView
#To enable the password change form to work, import below and use
from django.contrib.auth import views as auth_views
#The above will allow us to use some of the views that come with default django auth system
#If u need to know more, checkout videos on django auth system
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #Use the auth views with the default PasswordchangeView since it has already been implemented by default
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view()),
    #If you don't pass a custom template name as argument into the above, it will use the django custom template 
    #which is ugly and riddled with django stamps
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]
 