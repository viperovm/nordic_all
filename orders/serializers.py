from rest_framework import serializers
from .models import Orders
from django.core.mail import send_mail
from mail.models import UserList
import datetime

from django.template.loader import get_template
from django.core import mail
connection = mail.get_connection()


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'

    def create(self, validated_data):
        instance = super(OrdersSerializer, self).create(validated_data)
        mail_list = UserList.objects.values_list('email', flat=True)
        if instance.email not in mail_list:
            user = UserList(name=instance.name, email=instance.email)
            user.save()

        context = {
            'data': instance,
            'year': datetime.date.today().year,
        }
        connection.open()
        try:
            send_mail(
                'Заказ Nordic Way',
                get_template('client_order_template_text.html').render(context),
                'Nordic Way магазин комбинезонов <sales@nordicway.ru>',
                [instance.email],
                connection=connection,
                fail_silently=False,
            )
            instance.messages_sent += 1
        except Exception as e:
            print(e)

        try:
            send_mail(
                'Новый заказ',
                get_template('admin_order_template_text.html').render(context),
                'Новый заказ! <sales@nordicway.ru>',
                ['s.dolganin@mail.ru', 'viperovm@yandex.ru', 'sales@nordicway.ru'],
                connection=connection,
                fail_silently=False,
            )
            instance.messages_sent += 1
        except Exception as e:
            print(e)

        connection.close()
        instance.save()
        return instance
