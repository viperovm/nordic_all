from django.db import models


class FaqElement(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', null=True, blank=True)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент ЧаВо'
        verbose_name_plural = 'Элементы ЧаВо'
        ordering = ['id']


class ExtraElement(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', null=True, blank=True)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Доп Элемент'
        verbose_name_plural = 'Доп Элементы'
        ordering = ['id']
