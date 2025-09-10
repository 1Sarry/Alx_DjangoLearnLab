from django.urls import path
from .views import FeedAPIView, CreatePostAPIView

urlpatterns = [
    path('feed/', FeedAPIView.as_view(), name='feed'),
    path('posts/create/', CreatePostAPIView.as_view(), name='create-post'),
]