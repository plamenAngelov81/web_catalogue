from django.contrib import admin

from web_shop_0_1.user_profile.models import UserProfile


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', "age"]
    search_fields = ['username']
    list_filter = ['username', 'first_name', 'last_name']
    fieldsets = (
        ('LogIn', {'fields': ('username',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'age')}),
        ('Delivery info', {'fields': ('phone_number', 'user_address')}),
        ('Group Info', {'fields': ('groups', 'is_staff')})
    )
    list_display_links = ('username', 'first_name', 'last_name')
