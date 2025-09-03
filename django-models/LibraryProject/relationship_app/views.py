from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', context={'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'relationship_app/register.html'

class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"
    redirect_field_name = True
    success_url = reverse_lazy('home')

def logout_view(request):
    return render(request, 'relationship_app/logout.html')

def home(request):
    return render(request, 'relationship_app/home.html')