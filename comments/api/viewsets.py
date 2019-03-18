from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from .serializers import ComentSerializer


class ComentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ComentSerializer