from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', list_books, name='list-books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail')
]