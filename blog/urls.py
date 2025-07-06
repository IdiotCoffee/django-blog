from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="home"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.singleBlog, name="singlepost")
                    
]