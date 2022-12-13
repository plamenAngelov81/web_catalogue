import django_filters
from .models import *


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = ['product_type', 'diameter', 'length', 'color']