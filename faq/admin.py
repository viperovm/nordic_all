from django.contrib import admin
from .models import FaqElement, ExtraElement


class FaqElementAdmin(admin.ModelAdmin):
    model = FaqElement
    list_display = ('title',)
    list_display_links = ('title',)


class ExtraElementAdmin(admin.ModelAdmin):
    model = ExtraElement
    list_display = ('title',)
    list_display_links = ('title',)


admin.site.register(FaqElement, FaqElementAdmin)
admin.site.register(ExtraElement, ExtraElementAdmin)
