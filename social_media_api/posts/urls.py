from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('follow/<int:id>/', views.FollowView.as_view(), name='follow'),
    path('unfollow/<int:id>/', views.UnfollowView.as_view(), name='unfollow')
]
