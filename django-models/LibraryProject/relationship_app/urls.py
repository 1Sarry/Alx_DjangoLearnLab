from django.urls import path
from . import views
from .views import BookListView


urlpatterns = [
    path('book_list/', views.book_list),
    path('book_list_detail/', BookListView.as_view(), name = 'book_list')
]