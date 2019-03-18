from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from attractions.models import Attraction
from .serializers import AtractionSerializer


class AtractionViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AtractionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'description')