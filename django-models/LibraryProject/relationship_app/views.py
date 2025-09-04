from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Library, Book
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', context={'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('home'))
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


def home(request):
    return render(request, 'relationship_app/home.html')

user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')