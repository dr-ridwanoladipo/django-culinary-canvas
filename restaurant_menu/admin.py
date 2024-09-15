from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Item model.
    """
    list_display = ("meal", "status")
    list_filter = ("status", )
    search_fields = ("meal", "description")


admin.site.register(Item, MenuItemAdmin)
