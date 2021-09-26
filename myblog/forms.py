from django import forms
from .models import Post, Category, Comment

#choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainments', 'entertainments'),]
#The above is how to hard code a select button and pass it as argument to category(choices=choices),
#You call it twice. The drawback is that it isn't dynamic
choices = Category.objects.all().values_list('name', 'name')#You call the tuple twice

choice_list = []
for item in choices:
    choice_list.append(item)


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        #fields = '__all__'#If you do all, u cant arrange it according to how you want it displayed on ur page
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 
             'placeholder': 'This is for your titles, something fancy'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '',
             'id': 'writer', 'type': 'hidden'}),
             #The above code (author) will use javascript to assign the value of the logged in user to 
             #the backend, the script is embedded on the template.
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdatePostform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is for your titles, something fancy'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'category': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is for your titles, something fancy'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }