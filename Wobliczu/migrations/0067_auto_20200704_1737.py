# Generated by Django 3.0.5 on 2020-07-04 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0066_auto_20200704_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='publication_date',
            new_name='when_to_public',
        ),
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 4, 17, 37, 8, 771801)),
        ),
    ]
