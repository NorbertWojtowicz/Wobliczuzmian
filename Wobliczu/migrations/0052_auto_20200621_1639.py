# Generated by Django 3.0.5 on 2020-06-21 14:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0051_auto_20200617_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 16, 39, 5, 265409)),
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=35, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=999, null=True)),
                ('comment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Wobliczu.Comment')),
            ],
        ),
    ]
