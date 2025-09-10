from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like
from django.contrib.contenttypes.models import ContentType
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from notifications.models import Notification
User = get_user_model()

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class CreatePostAPIView(generics.CreateAPIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer_class = PostSerializer
        serializer.save(author=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Save comment with the logged-in user as author
        comment = serializer.save(author=self.request.user)

        # Get the post this comment is attached to
        post = comment.post  

        # Don’t notify if user comments on their own post
        if post.author != self.request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb='commented on your post',
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id
            )


class FeedAPIView(APIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)


class LikePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post =  generics.get_object_or_404(Post, pk=pk)
        user = request.user
        # Prevent liking own post if you want (optional). We'll allow it but no notification if same user.
        if Like.objects.filter(post=post, user=user).exists():
            return Response({"detail": "Already liked."}, status=status.HTTP_400_BAD_REQUEST)
        like, created = Like.objects.created(post=post, user=request.user)

        # Create notification for post author (don't notify if author liked their own post)
    def post(self, request, pk, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=pk)  # ✅ get post
        like, created = Like.objects.get_or_create(user=request.user, post=post)  # ✅ like or get

        if created:
            # Notify post author (but not if they liked their own post)
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb="liked your post",
                    target_content_type=ContentType.objects.get_for_model(post),
                    target_object_id=post.id
                )
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "You already liked this post"}, status=status.HTTP_200_OK)
        

class UnlikePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        like_qs = Like.objects.filter(post=post, user=user)
        if not like_qs.exists():
            return Response({"detail": "Not liked yet."}, status=status.HTTP_400_BAD_REQUEST)
        # delete like
        like_qs.delete()
        
        Notification.objects.filter(
            recipient=post.author,
            actor=user,
            verb__icontains='liked',
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        ).delete()
        return Response({"detail": "Unliked."}, status=status.HTTP_200_OK)