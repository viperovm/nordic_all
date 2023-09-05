# Generated by Django 4.1.1 on 2022-11-18 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('errors', '0001_initial'),
        ('mail', '0002_mail_counter_mail_heading_mail_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='counter',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='errors.massmailsuccess', verbose_name='Писем отправлено'),
        ),
    ]
