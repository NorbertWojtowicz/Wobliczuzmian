# Generated by Django 3.0.5 on 2020-07-03 23:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0064_auto_20200704_0055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publication_date',
        ),
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 4, 1, 6, 59, 489439)),
        ),
    ]
