from rest_framework.viewsets import ModelViewSet
from evaluation.models import Evaluating
from .serializers import EvaluantionSerializer


class EvaluationViewSet(ModelViewSet):
    queryset = Evaluating.objects.all()
    serializer_class = EvaluantionSerializer