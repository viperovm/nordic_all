from django.db import models


class OrderMailErrors(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', null=True, blank=True)
    email = models.CharField(max_length=255, verbose_name='Email', null=True, blank=True)
    date = models.DateTimeField(verbose_name='Дата и время ошибки', auto_now=True, null=True, blank=True)
    text = models.TextField(verbose_name='Текст ошибки', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ошибка оповещения о заказе'
        verbose_name_plural = 'Ошибки оповещений о заказах'


class OrderSaveErrors(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', null=True, blank=True)
    date = models.DateTimeField(verbose_name='Дата и время ошибки', auto_now=True, null=True, blank=True)
    text = models.TextField(verbose_name='Текст ошибки', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ошибка сохранения заказа'
        verbose_name_plural = 'Ошибки сохранения заказов'


class MassMailErrors(models.Model):
    subject = models.CharField(max_length=250, verbose_name='Наименование рассылки', null=True, blank=True)
    email = models.CharField(max_length=255, verbose_name='Email', null=True, blank=True)
    date = models.DateTimeField(verbose_name='Дата и время ошибки', auto_now=True, null=True, blank=True)
    text = models.TextField(verbose_name='Текст ошибки', null=True, blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Ошибка при массовой рассылке'
        verbose_name_plural = 'Ошибки при массовой рассылке'


class MassMailSuccess(models.Model):
    number = models.PositiveIntegerField(verbose_name='Отправлено сообщений', null=True, blank=True, default=0)
    name = models.CharField(max_length=255, verbose_name='Имя', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Результат массовой рассылки'
        verbose_name_plural = 'Результаты массовой рассылки'
