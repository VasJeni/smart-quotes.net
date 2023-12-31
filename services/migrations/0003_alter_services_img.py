# Generated by Django 4.0.10 on 2023-12-29 16:47

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_services_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=1048576, quality=-1, scale=None, size=[400, 600], upload_to='servicePic'),
        ),
    ]
