from django.db import models
from django.core.validators import MinLengthValidator


class CompanyInfo(models.Model):
    DAY_LEN = 15
    WORK_TYPE_TIME = 15
    CONTACT_MAX_LEN = 11
    CONTACT_MIN_LEN = 10
    ADDRESS_MAX_LEN = 150
    CITY_MAX_LEN = 30
    ADDRESS_MIN_LEN = 10
    CITY_MIN_LEN = 2

    work_time_name = models.CharField(
        verbose_name="Work type",
        max_length=WORK_TYPE_TIME,
        null=False,
        blank=False,
    )

    start_day = models.CharField(
        max_length=DAY_LEN,
        verbose_name='Start Day',
        null=False,
        blank=False,
    )

    end_day = models.CharField(
        max_length=DAY_LEN,
        verbose_name='End Day',
        null=False,
        blank=False,
    )

    start_shift = models.IntegerField(
        verbose_name='Start Shift',
        null=False,
        blank=False
    )

    end_shift = models.IntegerField(
        verbose_name='End Shift',
        null=False,
        blank=False
    )

    company_email = models.EmailField(
        verbose_name='Email',
        null=False,
        blank=False
    )

    contact = models.CharField(
        max_length=CONTACT_MAX_LEN,
        verbose_name='Contact',
        null=False,
        blank=False,
        validators=[MinLengthValidator(CONTACT_MIN_LEN)]
    )

    city = models.CharField(
        max_length=CITY_MAX_LEN,
        verbose_name='City',
        null=False,
        blank=False,
        validators=[MinLengthValidator(CITY_MIN_LEN)]
    )

    address = models.CharField(
        max_length=ADDRESS_MAX_LEN,
        verbose_name='Address',
        null=False,
        blank=False,
        validators=[MinLengthValidator(ADDRESS_MIN_LEN)]
    )

    def __str__(self):
        return self.work_time_name

    class Meta:
        verbose_name_plural = 'Company Info'


class Supplier(models.Model):
    MAX_SUPPLIER_NAME_LEN = 30

    supplier_name = models.CharField(
        max_length=MAX_SUPPLIER_NAME_LEN,
        verbose_name="Supplier",
        null=False,
        blank=False
    )

    supplier_number = models.IntegerField(
        verbose_name='Supplier Number',
        null=False,
        blank=False
    )

    supplier_address = models.TextField(
        verbose_name="Address",
        null=False,
        blank=False
    )

    def __str__(self):
        return self.supplier_name


class Messages(models.Model):
    TITLE_MAX_LEN = 50

    some_email = models.EmailField(
        verbose_name='Email',
        null=False,
        blank=False,
    )

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        verbose_name='Title',
        null=False,
        blank=False,
    )

    message = models.TextField(
        verbose_name='Your message',
        null=False,
        blank=False,
    )

    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Messages'
