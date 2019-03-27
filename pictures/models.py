import os
from django.db import models
from datetime import datetime


# Create your models here.
class Pictures(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='pictures/static/pictures/pix', default=str,
    null=bool)
    loaddress = photo.name
    upload_time = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.photo
    class Meta:
        verbose_name_plural = "Pictures"
