from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Orders


class OrdersResource(resources.ModelResource):

    class Meta:
        model = Orders


class OrdersAdmin(ImportExportModelAdmin):
    resource_classes = [OrdersResource]
    list_display = ('name', 'phone', 'email', 'shipping', 'date', 'is_completed')
    list_display_links = ('name',)
    readonly_fields = ('date', 'messages_sent')


admin.site.register(Orders, OrdersAdmin)
