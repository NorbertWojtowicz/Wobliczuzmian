# Generated by Django 3.0.5 on 2020-06-21 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0052_auto_20200621_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreply',
            name='article_slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 16, 46, 18, 293848)),
        ),
    ]
