from django.db import models
from utils.image_crop import create_crop_wout_tmb, get_tmb_path
import os
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from unidecode import unidecode
from django.utils.text import slugify


def image_directory_path(instance, filename):
    name, extension = os.path.splitext(filename)
    folder = 'goods_images'
    if len(folder) > 75:
        folder = folder[:75]
    return '{0}/{1}{2}'.format(folder, slugify(unidecode(name)), '.jpg')


class GoodsCategory(models.Model):
    name = models.CharField(_('Категория товара'), max_length=70, null=True, blank=True)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ['id']

    def __str__(self):
        return self.name


class GoodsSize(models.Model):
    size = models.CharField(max_length=4, verbose_name='Размер', null=True, blank=True)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.size


class Goods(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название товара', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True, blank=True)
    new_price = models.PositiveIntegerField(verbose_name='Новая цена', null=True, blank=True)
    discount = models.PositiveIntegerField(verbose_name='Размер скидки', null=True, blank=True)
    new = models.BooleanField(verbose_name='Новинка',)
    description = models.TextField(verbose_name='Описание товара', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name='Категория товара', related_name='category',
                              blank=True)
    size = models.ManyToManyField(GoodsSize, verbose_name='Размеры',
                                   related_name='goods_sizes',
                                   null=True, blank=True)
    my_order = models.PositiveIntegerField(verbose_name='Сорт.',
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['my_order']


class GoodsImages(models.Model):

    image = models.ImageField(verbose_name='Фото', max_length=255, upload_to=image_directory_path)
    image_goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='Товары', related_name='goods_gallery',
                                    null=True, blank=True)

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'
        ordering = ['id']

    def __str__(self):
        return self.image.path

    def save(self, *args, **kwargs):
        super(GoodsImages, self).save()
        if not os.path.isfile(get_tmb_path(self)):
            create_crop_wout_tmb(self)


