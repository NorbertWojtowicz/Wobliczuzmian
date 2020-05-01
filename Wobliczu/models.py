from django.db import models

# Create your models here.

class Article(models.Model):
    ID = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=256)
    header = models.CharField(max_length=256)
    content = models.TextField()
    miniature = models.ImageField(upload_to='media/miniatures/')
    main_image = models.ImageField(upload_to='media/main_images/')

class ArticleImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/gallery/', verbose_name='image')