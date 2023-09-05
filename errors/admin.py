from django.contrib import admin
from .models import OrderMailErrors, OrderSaveErrors, MassMailErrors, MassMailSuccess


class OrderMailErrorsAdmin(admin.ModelAdmin):
    model = OrderMailErrors
    list_display = ('name', 'email', 'date')
    list_display_links = ('name',)


class OrderSaveErrorsAdmin(admin.ModelAdmin):
    model = OrderSaveErrors
    list_display = ('name', 'date')
    list_display_links = ('name',)


class MassMailErrorsAdmin(admin.ModelAdmin):
    model = MassMailErrors
    list_display = ('subject', 'email', 'date')
    list_display_links = ('subject',)


class MassMailSuccessAdmin(admin.ModelAdmin):
    model = MassMailSuccess
    list_display = ('name', 'number')
    list_display_links = ('name',)


admin.site.register(OrderMailErrors, OrderMailErrorsAdmin)
admin.site.register(OrderSaveErrors, OrderSaveErrorsAdmin)
admin.site.register(MassMailErrors, MassMailErrorsAdmin)
admin.site.register(MassMailSuccess, MassMailSuccessAdmin)