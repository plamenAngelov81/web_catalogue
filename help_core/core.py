# from django.core.validators import ValidationError
from web_shop_0_1.products.models import Products


class HelpCore:
    @staticmethod
    def item_position(some_query_set):
        rows = []
        per_row = 5

        for i in range(0, len(some_query_set), per_row):
            current_row = some_query_set[i: i + per_row]
            rows.append(current_row)
        return rows

    @staticmethod
    def get_product_set(product_type):
        result = Products.objects.filter(product_type__type_name=product_type)
        return result

    @staticmethod
    def get_context(item_type):
        title = item_type
        items = HelpCore.get_product_set(title)
        position = HelpCore.item_position(items)
        context = {
            'items': items,
            'positions': position,
            'title': title
        }
        return context
