# Generated by Django 3.0.5 on 2020-07-03 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0060_auto_20200703_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 3, 18, 52, 18, 992608)),
        ),
    ]
