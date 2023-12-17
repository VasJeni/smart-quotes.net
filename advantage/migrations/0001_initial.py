# Generated by Django 4.0.10 on 2023-12-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adventage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=200)),
                ('description_en', models.CharField(max_length=400)),
                ('title_uk', models.CharField(max_length=200)),
                ('description_uk', models.CharField(max_length=400)),
                ('img', models.ImageField(blank='true', upload_to='images/adventagePic/')),
            ],
        ),
    ]