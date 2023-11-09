from django.contrib import admin
from .models import Blog_post
from .forms import CategoryForm


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    
@admin.register(Blog_post)
class BlogPostAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('blog_title', 'posted_by', 'pub_date', 'category')  

