import logging
import os

from django.conf import settings
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView

from converter.serializers.converter import ConvertFileSerializer, ConvertLinkSerializer

logger = logging.getLogger(__name__)


class ConvertView(CreateAPIView):
    def get_serializer_class(self):
        if self.request.data.get('link', None):
            return ConvertLinkSerializer

        return ConvertFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        converted_file = serializer.save()

        file_path = os.path.join(settings.MEDIA_ROOT, converted_file.result_file.name)
        filename = 'result.pdf'
        with open(file_path, 'rb') as f:
            response = HttpResponse(f, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
