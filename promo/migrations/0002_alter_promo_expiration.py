# Generated by Django 4.1.1 on 2023-02-27 01:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='expiration',
            field=models.DateField(default=datetime.date(2023, 2, 27), verbose_name='Действителен до'),
        ),
    ]
