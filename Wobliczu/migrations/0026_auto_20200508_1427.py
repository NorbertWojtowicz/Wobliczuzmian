# Generated by Django 3.0.5 on 2020-05-08 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0025_auto_20200508_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text_section_four',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='text_section_three',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='text_section_two',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 14, 27, 25, 218602)),
        ),
    ]
