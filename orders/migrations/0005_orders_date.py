# Generated by Django 4.1.1 on 2022-11-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orders_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата и время заказа'),
        ),
    ]
