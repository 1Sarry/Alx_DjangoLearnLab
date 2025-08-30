from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
@permission_required('your_app_name.can_create', raise_exception=True)
def books_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Book.objects.create(title=title, content=content, created_by=request.user)
        return redirect("article_list")
    return render(request, "articles/create.html")

@permission_required('bookshelf.can_edit', raise_exception=True)
def books_edit(request, pk):
    books = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        books.title = request.POST.get("title")
        books.content = request.POST.get("content")
        books.save()
        return redirect("books_list")
    return render(request, "books/edit.html", {"article": books})

@permission_required('bookshelf.can_delete', raise_exception=True)
def books_delete(request, pk):
    books = get_object_or_404(Book, pk=pk)
    books.delete()
    return redirect("books_list")
