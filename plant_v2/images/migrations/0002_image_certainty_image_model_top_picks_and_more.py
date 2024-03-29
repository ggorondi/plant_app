# Generated by Django 5.0.2 on 2024-02-29 14:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='certainty',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='model_top_picks',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='scientific_name',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.validate_image_file_extension]),
        ),
    ]
