from django.db import models
from django.core.validators import FileExtensionValidator


class Resume(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='resume/',
                            validators=[FileExtensionValidator(
                                allowed_extensions=['doc', 'pdf', 'docx'])])
    skills = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
