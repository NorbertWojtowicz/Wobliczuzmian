# Generated by Django 3.0.5 on 2020-05-05 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0012_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 5, 23, 11, 25, 729102)),
        ),
    ]
