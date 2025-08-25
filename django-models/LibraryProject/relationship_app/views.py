from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import BookForm
# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
   model = Library
   template_name = 'relationship_app/library_detail.html' 
   context_object_name = 'library'

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            form = UserCreationForm()
        return render(request, "relationship_app/register.html", {"form": form})
    
class LoginView(LoginView):
    template_name = "relationship_app/login.html"

class LogoutView(LogoutView):
    template_name = "relationship_app/logout.html"



#Role based views

def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "member"


# ----Views-----

@login_required
@user_passes_test(is_librarian)
def librarian_page(request):
    return render(request, "relationship_app/librarian_view.html")


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "relationship_app/admin_view.html")


@login_required
@user_passes_test(is_member)

def member_page(request):
    return(request, "relationship_app/member_view.html")



# Add Book View

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form', form})


# --- Edit Book View ---
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})


# --- Delete Book View ---
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})