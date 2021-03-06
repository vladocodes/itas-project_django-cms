from django import forms
from .models import Category, Comment, Post


choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for i in choices:
    choice_list.append(i)

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'add-post-form'}),
            'author': forms.Select(attrs = {'class': 'add-post-form'}),
            'category': forms.Select(choices = choice_list, attrs = {'class': 'add-post-form'}),
            'body': forms.Textarea(attrs = {'class': 'add-post-form'}),
        }

class editForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'add-post-form'}),
            'category': forms.Select(choices = choice_list, attrs = {'class': 'add-post-form'}),
            'body': forms.Textarea(attrs = {'class': 'add-post-form'}),
        }


class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
    
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'comment-input-name', 'placeholder': 'Unesite ime'}),
            'email': forms.TextInput(attrs = {'class': 'comment-input-mail', 'placeholder': 'Unesite email'}),
            'body': forms.Textarea(attrs = {'class': 'comment-input-body', 'placeholder': 'Unesite komentar...'}),
        }
        labels = {
            'name': 'Ime',
            'email': 'Email',
            'body': 'Komentar'
        }
