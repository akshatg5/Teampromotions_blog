from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Blog_post
from django.core.paginator import Paginator

# Create your views here.

def blog(request):
    categories = Blog_post.objects.values('category').distinct()
    
    category_counts = {}
    for category in categories:
        category_name = category['category']
        post_count = Blog_post.objects.filter(category=category_name).count()
        category_counts[category_name] = post_count
    
    #Dealing with the Posts:
    blog_posts = Blog_post.objects.all().order_by('pub_date').reverse()
    
    #adding pagination
    paginator = Paginator(blog_posts,5)
    pagenum = request.GET.get('page')
    posts_on_the_page = paginator.get_page(pagenum)
    
    return render(request,"layout.html",{'blog_posts' : posts_on_the_page,'category_counts':category_counts})

def post_page(request,post_id):
    post = get_object_or_404(Blog_post,pk=post_id)
    # blog_posts = Blog_post.objects.all()
    
    categories = Blog_post.objects.values('category').distinct()
    
    category_counts = {}
    for category in categories:
        category_name = category['category']
        post_count = Blog_post.objects.filter(category=category_name).count()
        category_counts[category_name] = post_count
        
    # blog_posts = Blog_post.objects.all().order_by('pub_date').reverse()
    
    previous_post = Blog_post.objects.filter(pub_date__lt=post.pub_date).order_by('-pub_date').first()    
    next_post = Blog_post.objects.filter(pub_date__gt=post.pub_date).order_by('pub_date').first()    
    
    return render(request,"blogpage.html",{'post' : post, 'post_id' : post_id,'previous_post':previous_post,'next_post':next_post , 'category_counts' : category_counts})