from django.shortcuts import render
from .models import Book, Library
from django.views.generic import ListView, DetailView
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


class BookListView(DetailView):
   model = Book
   template = 'library_detail.html' 
   context_object_name = 'library'

