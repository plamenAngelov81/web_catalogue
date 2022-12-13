from django.contrib import admin

from web_shop_0_1.company_info.models import CompanyInfo, Supplier, Messages


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ["work_time_name"]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['supplier_name', 'supplier_number']


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['title']
