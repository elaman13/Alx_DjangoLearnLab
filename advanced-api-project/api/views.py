# from django.shortcuts import render
# from django.views import generic
# from . import models
# from django.urls import reverse_lazy

# # Create your views here.
# class BookListView(generic.ListView):
#     model = models.Book
#     template_name = 'api/book_list.html'
#     context_object_name = 'books'

# class BookDetailView(generic.DetailView):
#     model = models.Book
#     template_name = 'api/book_detail.html'
#     context_object_name = 'book'

# class BookCreateView(generic.CreateView):
#     model = models.Book
#     fields = '__all__'
#     template_name = 'api/book_create.html'
#     success_url = reverse_lazy('book-list')
#     context_object_name = 'form'

# class BookUpdateView(generic.UpdateView):
#     model = models.Book
#     fields = '__all__'
#     template_name = 'api/book_update.html'
#     success_url = reverse_lazy('book-list')
#     context_object_name = 'form'
    
# class BookDeleteView(generic.DeleteView):
#     model = models.Book
#     template_name = 'api/book_delete.html'
#     success_url = reverse_lazy('book-list')

# api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books → read-only
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # everyone can see

# Retrieve single book → read-only
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book → authenticated only
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update existing book → authenticated only
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete book → authenticated only
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
