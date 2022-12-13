from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from web_shop_0_1.company_info.models import Supplier


class ProductClass(models.Model):
    MAX_LEN = 25
    MIN_LEN = 3

    class_name = models.CharField(
        max_length=MAX_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(MIN_LEN)]
    )

    class Meta:
        verbose_name_plural = 'Product Class'

    def __str__(self):
        return self.class_name


class ProductType(models.Model):
    MAX_LEN = 25
    MIN_LEN = 3

    type_name = models.CharField(
        max_length=MAX_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(MIN_LEN)]
    )

    class Meta:
        verbose_name_plural = 'Product Type'

    def __str__(self):
        return self.type_name


class Products(models.Model):
    MAX_LEN = 25
    MIN_LEN = 3
    MIN_VALUE = 0

    name = models.CharField(
        verbose_name='Name',
        max_length=MAX_LEN,
        null=False,
        blank=False,
        validators=[MinLengthValidator(MIN_LEN)]
    )

    brand = models.CharField(
        verbose_name='Brand',
        max_length=MAX_LEN,
        null=False,
        blank=False,
        validators=[MinLengthValidator(MIN_LEN)]
    )

    product_class = models.ForeignKey(
        ProductClass,
        verbose_name='Product Class',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    product_type = models.ForeignKey(
        ProductType,
        verbose_name='Product Type',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    item_image = models.ImageField(
        upload_to='products',
        verbose_name='Image',
        null=True,
        blank=True
    )

    price = models.FloatField(
        verbose_name='Price',
        null=True,
        blank=True,
        validators=[MinValueValidator(MIN_VALUE)]
    )

    color = models.CharField(
        verbose_name='Color',
        max_length=MAX_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(MIN_LEN)]
    )

    quantity = models.FloatField(
        verbose_name='Quantity (litters)',
        null=True,
        blank=True,
        validators=[MinValueValidator(MIN_VALUE)]
    )

    length = models.FloatField(
        verbose_name='Length (mm)',
        null=True,
        blank=True,
        validators=[MinValueValidator(MIN_VALUE)]
    )

    width = models.FloatField(
        verbose_name='Width (mm)',
        null=True,
        blank=True,
        validators=[MinValueValidator(MIN_VALUE)]
    )

    height = models.FloatField(
        verbose_name='Height (mm)',
        null=True,
        blank=True,
        validators=[MinValueValidator(MIN_VALUE)]
    )

    weight = models.FloatField(
        verbose_name='Weight (kg)',
        null=True,
        blank=True,
        validators=[MinValueValidator(MIN_VALUE)]
    )

    diameter = models.FloatField(
        verbose_name='Diameter (mm)',
        null=True,
        blank=True,
        validators=[MinValueValidator(MIN_VALUE)]
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
