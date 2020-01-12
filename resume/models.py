from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Resume(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='resume/',
                            validators=[FileExtensionValidator(
                                allowed_extensions=['doc', 'pdf', 'docx'])])
    skills = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


# delete files from media in local or in production storage after resume instance deleted
# this signal worked perfectly on local but has problem on production so added django-cleanup
# @receiver(post_delete, sender=Resume)
# def resume_post_delete(sender, **kwargs):
#     resume = kwargs['instance']
#     storage, name = resume.file.storage, resume.file.name
#     storage.delete(name)
