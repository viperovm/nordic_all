# Generated by Django 4.1.1 on 2022-11-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0013_alter_goodscategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Размер скидки'),
        ),
        migrations.AddField(
            model_name='goods',
            name='new',
            field=models.BooleanField(default=0, verbose_name='Новинка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='new_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Новая цена'),
        ),
    ]
