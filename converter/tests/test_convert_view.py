import io
import shutil

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from converter.models import ConvertedLink, ConvertedFile

from unittest import mock


@override_settings(MEDIA_ROOT='media')
class ConverterViewTest(TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree('media')

    @mock.patch('converter.serializers.converter.html_link_to_pdf', return_value=b'test')
    def test_html_link_to_pdf(self, html_link_to_pdf_mock):
        link = 'https://test.com/'

        response = self.client.post(reverse('convert_document'), data={'link': link})

        html_link_to_pdf_mock.assert_called_with(link)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'test')
        self.assertEqual(response['Content-Type'], 'application/pdf')

        self.assertEqual(ConvertedLink.objects.count(), 1)
        c_obj = ConvertedLink.objects.first()
        self.assertEqual(c_obj.link, link)
        self.assertEqual(c_obj.result_file.read(), b'test')

    @mock.patch('converter.serializers.converter.html_str_to_pdf', return_value=b'test')
    def test_html_file_to_pdf(self, html_str_to_pdf_mock):
        html_str = '<html><h1>Test</h1></html>'

        stream = io.StringIO()
        stream.write(html_str)
        file_obj = SimpleUploadedFile('test.html', bytes(stream.getvalue(), 'utf-8'))

        response = self.client.post(reverse('convert_document'), data={'file': file_obj})

        html_str_to_pdf_mock.assert_called_with(html_str)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'test')
        self.assertEqual(response['Content-Type'], 'application/pdf')

        self.assertEqual(ConvertedFile.objects.count(), 1)
        c_obj = ConvertedFile.objects.first()
        self.assertEqual(c_obj.file.read().decode(), html_str)
        self.assertEqual(c_obj.result_file.read(), b'test')
