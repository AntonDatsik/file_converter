from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from core.utils.validators import FileFieldValidator


class ConverterViewParamsSerializer(serializers.Serializer):
    file = serializers.FileField(validators=(FileFieldValidator(extension='html'),), required=False)
    link = serializers.URLField(required=False)

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        if validated_data.get('file', None) is None and validated_data.get('link', None) is None:
            raise serializers.ValidationError(
                _('Either file or link should be passed as arguments.')
            )

        return validated_data
