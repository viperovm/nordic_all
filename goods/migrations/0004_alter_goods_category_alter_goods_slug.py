# Generated by Django 4.1.1 on 2022-10-04 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_goods_images_alter_goods_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.goodscategory', verbose_name='Категория товара'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
