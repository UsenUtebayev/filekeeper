from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class VideoModel(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True)
    videoUrl = models.FileField(upload_to='videos/%Y/%m/%d',
                                verbose_name="Видео",
                                blank=True,
                                null=False,
                                validators=[FileExtensionValidator(allowed_extensions=
                                                                   ['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ['-pk']
