from rest_framework import viewsets, filters, permissions, generics, status
from . import models
from . import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from django.shortcuts import get_object_or_404

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class FollowView(generics.GenericAPIView):
    serializer_class = serializers.FollowUnfollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        user = request.user
        added_user = get_object_or_404(get_user_model(), id=id)

        if user.id == added_user.id:
            raise ValidationError('You cannot follow yourself.')
        
        user.following.add(added_user)

        serializer = self.get_serializer(user.following.all(), many=True)
        print(f'serializer: {serializer}')
        return Response(serializer.data, status=status.HTTP_200_OK)

class UnfollowView(generics.GenericAPIView):
    serializer_class = serializers.FollowUnfollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        user = request.user
        get_unfollow_user = get_object_or_404(get_user_model(), id=id)

        if get_unfollow_user.id == user.id:
            raise ValidationError('You cannot unfollow yourself.')

        unfollow_user = get_object_or_404(user.following.all(), id=id)
        user.following.remove(unfollow_user)

        serializer = self.get_serializer(user.following.all(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
