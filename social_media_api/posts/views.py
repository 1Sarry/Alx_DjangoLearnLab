# posts/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer

User = get_user_model()

class CreatePostAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        follow_qs = user.following.all()
        feed_posts = Post.objects.filter(author__in=follow_qs.union(User.objects.filter(id=user.id))).order_by('-created_at')
        serializer = PostSerializer(feed_posts, many=True, context={'request': request})
        return Response(serializer.data)
