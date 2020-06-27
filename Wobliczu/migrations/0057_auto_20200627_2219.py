# Generated by Django 3.0.5 on 2020-06-27 20:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0056_auto_20200627_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 27, 22, 19, 3, 584223)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='number_of_replies',
            field=models.IntegerField(blank=True, default=0, max_length=3),
        ),
    ]
