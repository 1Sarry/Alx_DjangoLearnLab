from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView

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
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            form = UserRegisterForm()
        return render(request, "relationship_app/regiser.html", {"form": form})
    
class LoginView(LoginView):
    template_name = "relationship_app/login.html"

class LogoutView(LogoutView):
    template_name = "relationship_app/logout.html"