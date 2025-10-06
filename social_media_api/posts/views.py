from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from . import models
from . import serializers

# Create your views here.
class PostViewSet(ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return models.Post.objects.filter(id=user.id)