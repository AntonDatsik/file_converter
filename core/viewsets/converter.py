import logging

from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from core.converters import html_link_to_pdf, html_str_to_pdf
from core.serializers.converter import ConverterViewParamsSerializer

logger = logging.getLogger(__name__)


class ConvertDocumentView(GenericAPIView):
    serializer_class = ConverterViewParamsSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file_link = serializer.validated_data.get('link', None)
        file = serializer.validated_data.get('file', None)

        try:
            if file_link is not None:
                converted_file = html_link_to_pdf(file_link)
            else:
                converted_file = html_str_to_pdf(file.read().decode())
        except Exception as exc:
            logger.exception('Error has been occurred during converting file to PDF. %s', exc)
            return Response(_('Cannot generate file. Check your file or link.'), status=HTTP_400_BAD_REQUEST)

        filename = 'result.pdf'
        response = HttpResponse(converted_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
