from django.contrib.auth.views import LoginView
from django.urls import path
from .views import list_books, LibraryDetailView, SignUpView, home, login_view, logout_view

urlpatterns = [
    path('', list_books, name='list-books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', SignUpView.as_view(), name='register'),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]