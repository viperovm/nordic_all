# Generated by Django 4.1.1 on 2022-10-05 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_alter_goods_category_alter_goods_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsimages',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='images', to='goods.goods', verbose_name='Товары'),
        ),
    ]
