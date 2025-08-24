from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView


urlpatterns = [
    path('books/', list_books, name= 'book_list'),
    path('library/', LibraryDetailView.as_view(), name = 'library'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register', register, name='register')
]