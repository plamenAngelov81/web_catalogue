from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

PROJECT_CHOICES = (
    ('Courses', 'Courses'),
    ('Services', 'Services'),
)


class Project(models.Model):
    NAME_MAX_LEN = 35
    TYPE_MAX_LEN = 35
    NAME_MIN_LEN = 3
    TYPE_MIN_LEN = 3
    MIN_VALUE = 3

    name = models.CharField(
        verbose_name='Project Name',
        max_length=NAME_MAX_LEN,
        validators=[MinLengthValidator(NAME_MIN_LEN)],
        null=True,
        blank=True,
    )
    project_type = models.CharField(
        verbose_name='Project Type',
        max_length=TYPE_MAX_LEN,
        validators=[MinLengthValidator(TYPE_MIN_LEN)],
        null=True,
        blank=True,
        choices=PROJECT_CHOICES
    )

    active = models.BooleanField(
        verbose_name='Available',
        null=False,
        blank=False,
    )

    description = models.TextField(
        verbose_name='Description',
        null=False,
        blank=False,
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=[MinValueValidator(MIN_VALUE)],
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name
