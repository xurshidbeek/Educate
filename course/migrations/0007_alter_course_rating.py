# Generated by Django 5.0.7 on 2024-07-18 20:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_rename_speciality_speciality_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]