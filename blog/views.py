from django.shortcuts import render

# Create your views here.

def  homePage(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def singleBlog(request):
    pass