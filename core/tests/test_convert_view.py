import io

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from unittest import mock


class ConverterViewTest(TestCase):
    @mock.patch('core.viewsets.converter.html_link_to_pdf', return_value=b'test')
    def test_html_link_to_pdf(self, html_link_to_pdf_mock):
        response = self.client.post(reverse('convert_document'), data={'link': 'https://test.com/'})

        html_link_to_pdf_mock.assert_called_with('https://test.com/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'test')
        self.assertEqual(response['Content-Type'], 'application/pdf')

    @mock.patch('core.viewsets.converter.html_str_to_pdf', return_value=b'test')
    def test_html_file_to_pdf(self, html_str_to_pdf_mock):
        stream = io.StringIO()
        stream.write('<html><h1>Test</h1></html>')
        file_obj = SimpleUploadedFile('test.html', bytes(stream.getvalue(), 'utf-8'))

        response = self.client.post(reverse('convert_document'), data={'file': file_obj})

        html_str_to_pdf_mock.assert_called_with('<html><h1>Test</h1></html>')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'test')
        self.assertEqual(response['Content-Type'], 'application/pdf')
