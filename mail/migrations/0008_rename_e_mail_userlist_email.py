# Generated by Django 4.1.1 on 2022-11-28 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_mail_test_mailing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlist',
            old_name='e_mail',
            new_name='email',
        ),
    ]
