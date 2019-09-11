from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import re_path

from .viewsets.converter import ConvertView


urlpatterns = [
    re_path(r'^convert/', ConvertView.as_view(), name='convert_document'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
