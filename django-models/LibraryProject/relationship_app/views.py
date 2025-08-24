from django.shortcuts import render
from .models import Book, Library
from django.views.generic import ListView, DetailView
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


class BookListView():
   model = Book
   template = 'books/library_detail.html' 
   context_object_name = 'library'

