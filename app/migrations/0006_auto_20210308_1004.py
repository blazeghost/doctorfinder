# Generated by Django 3.1.6 on 2021-03-08 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210305_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Gender',
            field=models.CharField(default='SELECT', max_length=50),
        ),
    ]
