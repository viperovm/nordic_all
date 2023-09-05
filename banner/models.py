from django.db import models


class Banner(models.Model):
    text_1 = models.CharField(max_length=100, verbose_name='Текст 1', null=True, blank=True)
    text_2 = models.CharField(max_length=100, verbose_name='Текст 2', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Активный', default=False)

    def __str__(self):
        return self.text_1

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class Commercial(models.Model):
    title = models.CharField(max_length=20, verbose_name='Заголовок', null=True, blank=True)
    subtitle = models.CharField(max_length=20, verbose_name='Подзаголовок', null=True, blank=True)
    url = models.CharField(max_length=255, verbose_name='Ссылка', null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='images/')
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Активный', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рекламный блок'
        verbose_name_plural = 'Рекламные блоки'


class Slider(models.Model):
    pre_title = models.CharField(max_length=20, verbose_name='Предзаголовок', null=True, blank=True)
    title = models.CharField(max_length=20, verbose_name='Заголовок', null=True, blank=True)
    subtitle = models.CharField(max_length=50, verbose_name='Подзаголовок', null=True, blank=True)
    url = models.CharField(max_length=255, verbose_name='Ссылка', null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='images/')
    button_text = models.CharField(max_length=20, verbose_name='Текст кнопки', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Активный', default=False)
    my_order = models.PositiveIntegerField(verbose_name='Сорт.',
                                           default=0,
                                           blank=False,
                                           null=False,
                                           )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['my_order']
