from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.viewers, name='viewers'),
    path('edit/', views.editors, name='editors'),
    path('admin/', views.admins, name='admins')
]
