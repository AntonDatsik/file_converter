from django.db import models


def result_files_upload_path(_, filename):
    return f'result_files/{filename}'


class ConvertedAbstract(models.Model):
    """
    Abstract model. Holds time of conversion and converted files.
    """
    converted_at = models.DateTimeField(auto_now_add=True)
    result_file = models.FileField(upload_to=result_files_upload_path)

    class Meta:
        abstract = True


class ConvertedLink(ConvertedAbstract):
    link = models.URLField()


def input_files_upload_path(_, filename):
    return f'input_files/{filename}'


class ConvertedFile(ConvertedAbstract):
    file = models.FileField(upload_to=input_files_upload_path)
