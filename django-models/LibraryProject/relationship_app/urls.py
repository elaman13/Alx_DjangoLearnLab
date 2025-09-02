from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books),
    path('library/<int:pk>/', views.BooksInLibrary.as_view())
]