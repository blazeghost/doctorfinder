# Generated by Django 3.1.6 on 2021-03-10 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Education',
            field=models.CharField(default='Your Education', max_length=200),
        ),
    ]
