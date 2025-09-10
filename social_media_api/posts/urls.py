from django.urls import path, include
from .views import FeedAPIView, CreatePostAPIView, PostViewSet, CommentViewSet, LikePostAPIView, UnlikePostAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedAPIView.as_view(), name='feed'),
    path('posts/create/', CreatePostAPIView.as_view(), name='create-post'),
    path('posts/<int:pk>/like/', LikePostAPIView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', UnlikePostAPIView.as_view(), name='post-unlike'),
]