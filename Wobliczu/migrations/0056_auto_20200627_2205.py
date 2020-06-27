# Generated by Django 3.0.5 on 2020-06-27 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0055_auto_20200626_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='number_of_replies',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 27, 22, 5, 56, 578571)),
        ),
    ]