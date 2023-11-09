from django import forms 
from .models import Blog_post

class CategoryForm(forms.ModelForm):
    category = forms. ChoiceField(choices=[
        ('seo','SEO'),
        ('advertising','Advertising'),
        ('business','Business'),
        ('optimization','Optimization'),
        ('digital marketing','Digital Marketing'),
        ('social','Social'),
        ('keyword','Keyword'),
        ('strategy','Strategy'),
        ('audience','Audience')
    ])
    
    class Meta:
        model = Blog_post
        fields = '__all__'