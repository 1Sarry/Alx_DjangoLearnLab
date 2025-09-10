from django.urls import path, include
from .views import FeedAPIView, CreatePostAPIView
from rest_framework.routers import DefaultRouter, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedAPIView.as_view(), name='feed'),
    path('posts/create/', CreatePostAPIView.as_view(), name='create-post'),
]