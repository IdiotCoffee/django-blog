from django.shortcuts import render, get_object_or_404
from .models import Post

# def get_date(post):
#     return post['date']

# Create your views here.
# postslist = []

def  homePage(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] #the negative sign ensures a descending order.
    # sorted_posts = sorted(postslist,key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts" : latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts" : all_posts
    })

def singleBlog(request, slug):
    # id_post = next(post for post in postslist if post['slug'] == slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/singlepost.html", {
        "post" : identified_post,
        "tags": identified_post.tags.all()
    })