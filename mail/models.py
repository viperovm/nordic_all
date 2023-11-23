import os
# import datetime

from django.db import models
# from django.template.loader import get_template
from django.utils.text import slugify
from unidecode import unidecode

# from django.core import mail

# from mail.task import send_message

def image_directory_path(instance, filename):
    name, extension = os.path.splitext(filename)
    folder = 'template_images'
    if len(folder) > 75:
        folder = folder[:75]
    return '{0}/{1}{2}'.format(folder, slugify(unidecode(name)), '.jpg')


class Mail(models.Model):
    subject = models.CharField(max_length=250, verbose_name='Тема письма', null=True, blank=True)
    heading = models.CharField(max_length=250, verbose_name='Заголовок', null=True, blank=True)
    sub_heading = models.CharField(max_length=250, verbose_name='Подзаголовок', null=True, blank=True)
    text = models.TextField(verbose_name='Текст письма', null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', max_length=255, upload_to='images/')
    date = models.DateTimeField(verbose_name='Дата отправки', auto_now=True, null=True, blank=True)
    counter = models.IntegerField(verbose_name='Писем отправлено', default=0)
    test_mailing = models.BooleanField(verbose_name='Тестовая рассылка', default=False)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    # def save(self, *args, **kwargs):
    #     self.counter = 0
    #     super(Mail, self).save()
    #     context = {
    #         'data': self,
    #         'year': datetime.date.today().year,
    #     }
    #     html = get_template('mailing_list_template_html.html').render(context)
    #     text = get_template('mailing_list_template_text.html').render(context)
    #     if self.test_mailing:
    #         e_mail_list = UserList.objects.filter(test_user=True).values_list('email', flat=True)
    #     else:
    #         e_mail_list = UserList.objects.values_list('email', flat=True)
    #     for index, e_mail in enumerate(e_mail_list):
    #         send_message.delay(self.subject, html, text, e_mail)
    #         self.counter += 1
    #
    #     super(Mail, self).save()


class UserList(models.Model):
    name = models.CharField(max_length=70, verbose_name='Имя', null=True, blank=True)
    last_name = models.CharField(max_length=70, verbose_name='Фамилия', null=True, blank=True)
    email = models.EmailField(verbose_name='E-mail', null=True, blank=True)
    test_user = models.BooleanField(verbose_name='Тестовый поьзователь', default=False)
    mailings = models.ManyToManyField(Mail)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Список клиентов'



