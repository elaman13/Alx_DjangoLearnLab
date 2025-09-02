from django.urls import path
from .views import list_books, BooksInLibrary

urlpatterns = [
    path('', list_books, name='list-books'),
    path('library/<int:pk>/', BooksInLibrary.as_view())
]