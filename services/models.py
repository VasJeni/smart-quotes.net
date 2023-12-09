from django.db import models

# Create your models here.


class Services(models.Model):
    title_en = models.CharField(max_length=200)
    description_en = models.CharField(max_length=400)
    title_uk = models.CharField(max_length=200)
    description_uk = models.CharField(max_length=400)

    def __str__(self):
        return self.title_en