from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import TouristSpot
from .serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer
    queryset = TouristSpot.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('id', 'name', 'adresses', 'attractions',
                     'comments', 'evaluations')
