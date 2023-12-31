# Generated by Django 4.1.1 on 2023-02-03 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo', models.CharField(max_length=60, verbose_name='Промокод')),
                ('expiration', models.DateField(default=datetime.date(2023, 2, 3), verbose_name='Действителен до')),
                ('discount', models.PositiveIntegerField(blank=True, default=10, null=True, verbose_name='Размер скидки %')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Промокод',
                'verbose_name_plural': 'Промокоды',
                'ordering': ['-id'],
            },
        ),
    ]
