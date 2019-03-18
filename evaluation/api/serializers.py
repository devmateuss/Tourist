from rest_framework.serializers import ModelSerializer
from evaluation.models import Evaluating

class EvaluantionSerializer(ModelSerializer):
    class Meta:
        model = Evaluating
        fields = ('__all__')