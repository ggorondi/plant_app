from wsgiref.util import FileWrapper
from rest_framework import viewsets
from .serializers import ImageSerializer
from ..models import Image
from rest_framework.decorators import action

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # api/images
    # api/images/<pk>/

    # # api/images/<pk>/download/
    # @action(detail=True, methods=['GET'])
    # def download(self, request, pk=None):
    #     instance = self.get_object()
    #     img_path = instance.img.path
    #     with open(img_path, 'rb') as f:
    #         return HttpResponse(FileWrapper(f), content_type="image/jpeg")
        
    # api/images/<pk>/plant_info/
    @action(detail=True, methods=['GET'])
    def download(self, request, pk=None):
        try:
            instance = self.get_object()
            return Response({'scientific_name': instance.scientific_name, 'certainty': f'{instance.certainty*100:.1f}%', 'model_top_picks': instance.model_top_picks})
        except Image.DoesNotExist:
            return Response({'error': 'Image not found'}, status=404)