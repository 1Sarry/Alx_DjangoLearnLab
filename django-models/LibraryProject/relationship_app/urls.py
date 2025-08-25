from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView


urlpatterns = [
    path('books/', list_books, name= 'book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('library/', LibraryDetailView.as_view(), name = 'library'),
    path('login/', LoginView.as_view(template_name=""), name="login"),
    path('logout/', LogoutView.as_view(template_name=""), name='logout'),
    path('register', views.register, name='register'),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('librarian_page/', views.librarian_page, name="librarian_page"),
    path('member_page/', views.member_page, name='member_page')
]