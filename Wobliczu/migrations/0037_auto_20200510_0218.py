# Generated by Django 3.0.5 on 2020-05-10 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0036_auto_20200510_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 2, 18, 31, 971821)),
        ),
    ]
