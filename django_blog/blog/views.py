from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'blog/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.CustomUserCreationForm()
    
    return render(request, 'blog/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'blog/home.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        
        user = request.user
        user.username= new_username
        user.email = new_email
        user.save()
        
        return redirect('profile')
        
    else:
        return render(request, 'blog/profile.html')

class PostListView(generic.ListView):
    model = models.Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = 'blog/posts_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin ,generic.CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'blog/post_create.html'
    login_url = 'login'
    success_url = reverse_lazy('posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(generic.UpdateView):
    model = models.Post
    template_name = 'blog/post_update.html'
    fields = ['title', 'author', 'content']
    success_url = reverse_lazy('posts')

class PostDeleteView(generic.DeleteView):
    model = models.Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts')