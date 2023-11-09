from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.blog, name='blog'),
    path("post_page/<int:post_id>", views.post_page, name='post_page')
]