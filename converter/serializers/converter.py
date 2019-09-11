import os
import uuid

from django.core.files.base import ContentFile, File
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.serializers import ValidationError

from converter.models import ConvertedAbstract, ConvertedFile, ConvertedLink
from converter.utils.validators import FileFieldValidator
from converter.converters import html_str_to_pdf, html_link_to_pdf


class ConvertSerializerMixin:
    @staticmethod
    def generate_unique_filename(filename: str) -> str:
        name, ext = os.path.splitext(filename)
        uid = uuid.uuid4()

        return f'{name}_{uid}{ext}'

    def save_converted_file(self, converted_file_obj: ConvertedAbstract, pdf_file: bytes) -> None:
        result_filename = self.generate_unique_filename('result.pdf')
        converted_file_obj.result_file.save(result_filename, ContentFile(pdf_file))


class ConvertFileSerializer(serializers.ModelSerializer, ConvertSerializerMixin):
    file = serializers.FileField(validators=(FileFieldValidator(extension='html'),), write_only=True)

    class Meta:
        model = ConvertedFile
        fields = 'file',

    def create(self, validated_data):
        file = validated_data['file']
        try:
            pdf_file = html_str_to_pdf(file.read().decode())
        except Exception:
            return ValidationError(_('Cannot generate file. Check your file.'))

        input_filename = self.generate_unique_filename(file.name)

        converted_file = ConvertedFile()
        converted_file.file.save(input_filename, File(file))

        self.save_converted_file(converted_file, pdf_file)
        converted_file.save()

        return converted_file


class ConvertLinkSerializer(serializers.ModelSerializer, ConvertSerializerMixin):
    link = serializers.URLField(write_only=True)

    class Meta:
        model = ConvertedLink
        fields = 'link',

    def create(self, validated_data):
        link = validated_data['link']

        converted_link = ConvertedLink(link=link)

        try:
            pdf_file = html_link_to_pdf(link)
        except Exception:
            return ValidationError(_('Cannot generate file. Check your link.'))

        self.save_converted_file(converted_link, pdf_file)
        converted_link.save()

        return converted_link
