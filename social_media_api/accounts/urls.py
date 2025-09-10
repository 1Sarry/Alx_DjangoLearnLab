from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProfileAPIView, FollowAPIView, UnfollowAPIView, FollowingListAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/<str:username>/', ProfileAPIView.as_view(), name='profile-detail'),
    path('follow/<int:user_id>/', FollowAPIView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnfollowAPIView.as_view(), name='unfollow'),
    path('following/', FollowingListAPIView.as_view(), name='my-following'),
    path('following/<int:user_id>/', FollowingListAPIView.as_view(), name='user-following'),
]