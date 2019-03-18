from rest_framework.serializers import ModelSerializer
from core.models import TouristSpot
from comments.api.serializers import ComentSerializer
from attractions.api.serializers import AtractionSerializer
from adresses.api.serializers import AddressSerializer


class TouristSpotSerializer(ModelSerializer):
    comments = ComentSerializer(many=True)
    attractions = AtractionSerializer(many=True)
    adresses = AddressSerializer()

    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'description', 'approved',
                  'photo', 'attractions', 'comments', 'evaluations', 'adresses')