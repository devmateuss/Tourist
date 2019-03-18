from rest_framework.serializers import ModelSerializer
from comments.models import Comment


class ComentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')