from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class Adventage(models.Model):
    title_en = models.CharField(max_length=200)
    description_en = models.CharField(max_length=400)
    title_uk = models.CharField(max_length=200)
    description_uk = models.CharField(max_length=400)
    img = models.FileField(
        upload_to="adventage/",
        blank="true",
        validators=[FileExtensionValidator(["svg", "png", "jpeg", "jpg"])],
    )

    def __str__(self) -> str:
        return self.title_en
