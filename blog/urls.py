from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.StartingPageView.as_view(), name="home"),
    path("posts", views.AllPostsView.as_view(), name="posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="singlepost"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
                    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)