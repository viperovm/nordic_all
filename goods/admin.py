from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from .models import GoodsImages, GoodsSize, GoodsCategory, Goods


class GoodsSizeAdmin(admin.ModelAdmin):
    model = GoodsSize
    list_display = ['size']
    list_display_links = ('size',)


class GoodsCategoryAdmin(admin.ModelAdmin):
    model = GoodsCategory
    list_display = ['name']
    list_display_links = ('name',)


class GoodsImageAdmin(admin.ModelAdmin):
    model = GoodsImages
    list_display = ('get_photo', 'get_goods_name')
    list_display_links = ('get_photo',)

    @admin.display(description='Миниатюра')
    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image}" width="55">')
        else:
            return '-'

    @admin.display(description='Товар')
    def get_goods_name(self, obj):
        if obj.image_goods:
            if obj.image_goods.name:
                return obj.image_goods.name
            else:
                return '-'
        else:
            return '-'


class GoodsImageInline(admin.TabularInline):
    model = GoodsImages
    readonly_fields = ('get_photo',)
    fieldsets = ((None, {'fields': ('get_photo', 'image')}),)
    extra = 4

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<a href={obj.image.url} target="_blank"><img src="{obj.image.url}" width="45"></a>')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


class GoodsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'category', 'new', 'price', 'my_order']
    list_filter = ('category',)
    inlines = [
        GoodsImageInline,
    ]


admin.site.register(GoodsImages)
admin.site.register(GoodsSize, GoodsSizeAdmin)
admin.site.register(GoodsCategory, GoodsCategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
