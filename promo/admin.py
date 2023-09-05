from django.contrib import admin
from import_export import resources
from .models import Promo


class PromoAdmin(admin.ModelAdmin):

    list_display = ['promo', 'discount', 'expiration', 'is_active']
    list_editable = ['discount', 'is_active']


admin.site.register(Promo, PromoAdmin)
