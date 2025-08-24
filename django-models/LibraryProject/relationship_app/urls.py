from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView


urlpatterns = [
    path('books/', list_books, name= 'book_list'),
    path('library/', LibraryDetailView.as_view(), name = 'library'),
    path('login/', LoginView.as_view(template_name=""), name="login"),
    path('logout/', LogoutView.as_view(template_name=""), name='logout'),
    path('register', views.register, name='register')
]