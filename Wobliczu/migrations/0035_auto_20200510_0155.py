# Generated by Django 3.0.5 on 2020-05-09 23:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0034_auto_20200510_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 1, 55, 18, 795886)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=1000, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Wobliczu.Article')),
            ],
        ),
    ]
