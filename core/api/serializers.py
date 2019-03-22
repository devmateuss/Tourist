from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import TouristSpot, DocumentIdentification
from comments.api.serializers import ComentSerializer
from attractions.api.serializers import AtractionSerializer
from adresses.api.serializers import AddressSerializer
from attractions.models import Attraction
from adresses.models import Address


class DocumentIdentificationSerializer(ModelSerializer):
    class Meta:
        model = DocumentIdentification
        fields = '__all__'


class TouristSpotSerializer(ModelSerializer):
    attractions = AtractionSerializer(many=True)
    adresses = AddressSerializer(read_only=True)
    description_complete = SerializerMethodField()
    document_Itentification = DocumentIdentificationSerializer()

    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'description', 'approved',
                  'photo', 'attractions', 'comments', 'evaluations', 'adresses'
                  'description_complete', 'document_Itentification')

    def create_atraction(self, atractions, point):
        for atraction in atractions:
            at = Attraction.objects.create(**atraction)
            point.attractions.add(at)

    def create(self, validated_data):
        attractions = validated_data['attractions']
        del validated_data['attractions']
        point = TouristSpot.object.create(**validated_data)

        adresses = validated_data['adresses']
        del validated_data['adresses']
        end = Address.objects.create(**adresses)

        document_Itentification = validated_data['document_Itentification']
        del validated_data['document_Itentification']
        doc = DocumentIdentification.objects.create(**document_Itentification)


        self.create_atraction(attractions, point)

        point.adresses = end
        point.document_Itentification = doc

        point.save()

        return point
