# Generated by Django 4.1.3 on 2022-11-30 20:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(blank=True, choices=[('Courses', 'Courses'), ('Services', 'Services')], max_length=35, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Project Type'),
        ),
    ]
