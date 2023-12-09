from django.db import models

# Create your models here.


class Feedback(models.Model):
    author = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    feedback_en = models.CharField(max_length=500)
    feedback_uk = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.company
