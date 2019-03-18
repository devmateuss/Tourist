from rest_framework.viewsets import ModelViewSet
from .serializers import AddressSerializer
from adresses.models import Address


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer