# Generated by Django 3.1.6 on 2021-03-10 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_doctor_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Address',
            field=models.CharField(default='Your Address', max_length=100),
        ),
    ]