from celery import shared_task

from django.core.mail import get_connection, EmailMultiAlternatives, send_mail

from errors.models import MassMailErrors
from .models import Mail, UserList

import datetime

from django.template.loader import get_template


@shared_task()
def send_message(mail_id):
    obj = Mail.objects.get(pk=mail_id)

    obj.counter += 1
    # obj.text = obj
    obj.save()

    # print(obj)
    #
    # context = {
    #     'data': obj,
    #     'year': datetime.date.today().year,
    # }
    # html = get_template('mailing_list_template_html.html').render(context)
    # text = get_template('mailing_list_template_text.html').render(context)
    #
    # if obj.test_mailing:
    #     e_mail_list = UserList.objects.filter(test_user=True).values_list('email', flat=True)
    # else:
    #     e_mail_list = UserList.objects.values_list('email', flat=True)
    #
    # for index, e_mail in enumerate(e_mail_list):
    #     try:
    #         send_mail(
    #             obj.subject,
    #             text,
    #             'Nordic Way магазин комбинезонов <sales@nordicway.ru>',
    #             [e_mail],
    #             html_message=html,
    #             fail_silently=False,
    #         )
    #         obj.counter += 1
    #         obj.save()
    #     except Exception as e:
    #         error = MassMailErrors(subject=obj.subject, email=e_mail, text=e)
    #         error.save()
    #         print(e)







# def send_message(subject, html, text, e_mail):
#     try:
#         send_mail(
#             subject,
#             text,
#             'Nordic Way магазин комбинезонов <sales@nordicway.ru>',
#             [e_mail],
#             html_message=html,
#             fail_silently=False,
#         )
#     except Exception as e:
#         return e
