# Generated by Django 3.1.6 on 2021-03-15 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_appoinment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='master_table',
            old_name='is_verifed',
            new_name='is_verified',
        ),
    ]
