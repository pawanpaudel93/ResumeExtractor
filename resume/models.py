from django.db import models
from django.core.validators import FileExtensionValidator


class Resume(models.Model):
    file = models.FileField(upload_to='resume/',
                            validators=[FileExtensionValidator(
                                allowed_extensions=['docx', 'pdf', 'docx'])])

    def __str__(self):
        return self.file.name.replace('resume/', '')
