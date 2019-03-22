from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import TouristSpot
from .serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer
    queryset = TouristSpot.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('id', 'name', 'adresses', 'attractions',
                     'comments', 'evaluations')
    lookup_field = 'id'

    @action(methods=['POST'], detail=True)
    def associate_atraction(self, request, id):
        atractions = request.data['ids']

        point = TouristSpot.objects.get(id=id)

        point.objects.set(atractions)

        point.save

        return Response(point)

