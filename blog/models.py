from django.db import models
from django.contrib.auth.models import AbstractUser
import markdown2

# Create your models here.
class Blog_post(models.Model):
    blog_title = models.CharField(max_length=250)
    posted_by = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")
    blog_images = models.ImageField(upload_to='blog_images/',default=None,blank=True, null=True)
    category = models.CharField(max_length=100)
    blog_post = models.TextField()
    
    def __str__(self):
        return f"{self.blog_title} by {self.posted_by}"
    
    
