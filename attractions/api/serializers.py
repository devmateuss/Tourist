from rest_framework.serializers import ModelSerializer
from attractions.models import Attraction


class AtractionSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('__all__')