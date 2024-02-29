from rest_framework import serializers
from ..models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'img','scientific_name','certainty','model_top_picks')