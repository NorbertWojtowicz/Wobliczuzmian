# Generated by Django 3.0.5 on 2020-07-03 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0062_auto_20200703_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 3, 19, 28, 7, 72454)),
        ),
    ]
