from django.contrib.auth.views import LoginView
from django.urls import path
from .views import list_books, LibraryDetailView, SignUpView, home, CustomLoginView, logout_view

urlpatterns = [
    path('', list_books, name='list-books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('signup/', SignUpView.as_view(template_name_field='relationship_app/library_detail.html'), name='signup'),
    path('home/', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view)
]