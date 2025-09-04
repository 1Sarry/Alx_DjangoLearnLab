from django.urls import path, include
from .views import(CustomBookCreateView, CustomBookUpdateView, CustomBookDeleteView, CustomBookDetailView, CustomBookListView) 

urlpatterns = [
    path('/books', CustomBookListView.as_view(), name='book-list-view'),
    path('/books/<int:pk>/', CustomBookDetailView.as_view(), name='book-detail-view'),
    path('/books/create/', CustomBookCreateView.as_view(), name='book-create-view'),
    path('/books/<int:pk>/update/', CustomBookUpdateView.as_view(), name='book-update-view'),
    path('/books/<int:pk>/delete/', CustomBookDeleteView.as_view(), name= 'book-delete-view')
]