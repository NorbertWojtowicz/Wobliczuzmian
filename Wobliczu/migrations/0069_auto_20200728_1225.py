# Generated by Django 3.0.5 on 2020-07-28 10:25

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0068_merge_20200711_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 12, 25, 10, 689252)),
        ),
    ]
