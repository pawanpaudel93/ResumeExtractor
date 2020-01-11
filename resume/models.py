from django.db import models


class Resume(models.Model):
    file = models.FileField(upload_to='resume/')