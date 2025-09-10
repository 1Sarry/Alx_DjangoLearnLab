# posts/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer

User = get_user_model()

class CreatePostAPIView(generics.CreateAPIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer_class = PostSerializer
        serializer.save(author=self.request.user)


class FeedAPIView(APIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)
