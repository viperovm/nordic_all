from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Banner, Commercial, Slider


class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ('text_1', 'text_2', 'is_active')
    list_display_links = ('text_1',)


class CommercialAdmin(admin.ModelAdmin):
    model = Commercial
    list_display = ('title', 'is_active')
    list_display_links = ('title',)


class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Slider
    list_display = ('title', 'is_active')
    list_display_links = ('title',)


admin.site.register(Banner, BannerAdmin)
admin.site.register(Commercial, CommercialAdmin)
admin.site.register(Slider, SliderAdmin)
