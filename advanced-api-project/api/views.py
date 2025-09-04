from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer
# Create your views here.


class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class CustomBookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CustomBookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class CustomBookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class CustomBookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



