from django.db import models
from django_resized import ResizedImageField

# Create your models here.


class Services(models.Model):
    img = ResizedImageField(
        upload_to="servicePic",
        blank=True,
        size=[400, 600],
        max_length=1048576,
    )
    title_en = models.CharField(max_length=200)
    description_en = models.CharField(max_length=400)
    title_uk = models.CharField(max_length=200)
    description_uk = models.CharField(max_length=400)

    def __str__(self):
        return self.title_en
