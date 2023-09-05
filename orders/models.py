from django.db import models
from datetime import date

from errors.models import OrderSaveErrors
from utils.image_crop import create_crop_wout_tmb, create_tmb, get_tmb_path
import os
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from unidecode import unidecode
from django.utils.text import slugify

from goods.models import Goods


class Orders(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя клиента', null=True, blank=True)
    city = models.CharField(max_length=255, verbose_name='Город', null=True, blank=True)
    address1 = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    address2 = models.CharField(max_length=255, verbose_name='Адрес дополнительно', null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон', null=True, blank=True)
    email = models.CharField(max_length=255, verbose_name='Email', null=True, blank=True)
    extra = models.TextField(verbose_name='Дополнительная информация', null=True, blank=True)
    orders = models.TextField(verbose_name='Заказы', null=True, blank=True)
    shipping = models.CharField(max_length=10, verbose_name='Доставка', null=True, blank=True)
    date = models.DateTimeField(verbose_name='Дата и время заказа', auto_now=True, null=True, blank=True)
    is_completed = models.BooleanField(verbose_name='Завершен', default=False)
    messages_sent = models.IntegerField(verbose_name='Писем отправлено', null=True, blank=True, default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            super(Orders, self).save()
        except Exception as e:
            err = OrderSaveErrors(name=self.name, text=e)
            err.save()


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

