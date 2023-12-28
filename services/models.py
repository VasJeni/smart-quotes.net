from django.db import models

# Create your models here.


class Services(models.Model):
    img = models.ImageField(
        upload_to="servicePic",
        blank=True,
        max_height=600,
        max_width=400,
        max_length=1048576,
    )
    title_en = models.CharField(max_length=200)
    description_en = models.CharField(max_length=400)
    title_uk = models.CharField(max_length=200)
    description_uk = models.CharField(max_length=400)

    def __str__(self):
        return self.title_en
