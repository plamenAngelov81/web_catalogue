from django.contrib import admin

from web_shop_0_1.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    radio_fields = {'project_type': admin.HORIZONTAL}
