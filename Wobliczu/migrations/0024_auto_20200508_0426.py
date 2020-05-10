# Generated by Django 3.0.5 on 2020-05-08 02:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Wobliczu', '0023_auto_20200506_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_section_four',
            field=models.ImageField(null=True, upload_to='media/sect4/'),
        ),
        migrations.AddField(
            model_name='article',
            name='image_section_three',
            field=models.ImageField(null=True, upload_to='media/sect3/'),
        ),
        migrations.AddField(
            model_name='article',
            name='image_section_two',
            field=models.ImageField(null=True, upload_to='media/sect2/'),
        ),
        migrations.AddField(
            model_name='article',
            name='text_section_four',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='text_section_three',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='text_section_two',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='main_tags',
            field=models.ManyToManyField(null=True, to='Wobliczu.MainTags'),
        ),
        migrations.AlterField(
            model_name='article',
            name='secondary_tags',
            field=models.ManyToManyField(null=True, to='Wobliczu.SecondaryTags'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Wobliczu.ArticleUser'),
        ),
        migrations.AlterField(
            model_name='articleuser',
            name='last_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 4, 26, 52, 734685)),
        ),
    ]