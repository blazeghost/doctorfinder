# Generated by Django 3.1.6 on 2021-03-08 05:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210308_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospitalname', models.CharField(max_length=50)),
                ('foundingyear', models.IntegerField(default='2020')),
                ('Contact', models.BigIntegerField(default='123')),
                ('website', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Intro', models.CharField(max_length=200)),
                ('hos_timing_from', models.TimeField(default=datetime.time(0, 0))),
                ('hos_timing_to', models.TimeField(default=datetime.time(0, 0))),
                ('logo', models.ImageField(default='/img/default-user.jpg', upload_to='img/')),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
            ],
        ),
    ]
