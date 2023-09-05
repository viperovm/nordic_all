from django.db import models
from datetime import date


class Promo(models.Model):
    promo = models.CharField(max_length=60, verbose_name='Промокод')
    expiration = models.DateField(default=date.today(), verbose_name='Действителен до')
    discount = models.PositiveIntegerField(default=10, null=True, blank=True, verbose_name='Размер скидки %')
    is_active = models.BooleanField(verbose_name='Активный', default=False)

    def __str__(self):
        return self.promo

    class Meta:
        ordering = ['-id']
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'
