# Generated by Django 3.0.5 on 2020-05-05 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0013_auto_20200505_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 23, 23, 45, 964185)),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 5, 23, 23, 45, 964185)),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]