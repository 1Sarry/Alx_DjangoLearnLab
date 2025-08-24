from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)


class BookListView():
   model = Book
   template = 'books/library_detail.html' 
   context_object_name = 'book_list'

