# Generated by Django 4.1.1 on 2022-12-11 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extraelement',
            options={'ordering': ['id'], 'verbose_name': 'Доп Элемент', 'verbose_name_plural': 'Доп Элементы'},
        ),
        migrations.AlterModelOptions(
            name='faqelement',
            options={'ordering': ['id'], 'verbose_name': 'Элемент ЧаВо', 'verbose_name_plural': 'Элементы ЧаВо'},
        ),
    ]
