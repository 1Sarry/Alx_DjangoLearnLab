from django.urls import path
from . import views
from .views import book_list, BookListView


urlpatterns = [
    path('books/', book_list, name= 'book_list'),
    path('library/', BookListView.as_view(), name = 'library')
]