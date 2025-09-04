from django.urls import path, include
from .views import CustomBookCreateView, CustomBookUpdateView, CustomBookDeleteView, CustomBookDetailView, CustomBookListView

urlpatterns = [
    path('/books', CustomBookListView.as_view(), name='book-list-view'),
    path('/books/<int:pk>/', CustomBookDetailView.as_view(), name='book-detail-view')
]