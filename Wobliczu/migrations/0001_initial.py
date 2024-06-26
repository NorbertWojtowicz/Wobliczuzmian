# Generated by Django 3.0.5 on 2020-05-01 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('short_desc', models.CharField(max_length=256)),
                ('header', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('miniature', models.ImageField(upload_to='media/miniatures/')),
                ('main_image', models.ImageField(upload_to='media/main_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/gallery/', verbose_name='image')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Wobliczu.Article')),
            ],
        ),
    ]
