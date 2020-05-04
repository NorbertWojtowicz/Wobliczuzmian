from django.db import models
# Create your models here.

class MainTags(models.Model):
    main_tag = models.CharField(max_length=20)
    def __str__(self):
        return self.main_tag

class SecondaryTags(models.Model):
    secondary_tag = models.CharField(max_length=20)
    def __str__(self):
        return self.secondary_tag

class Article(models.Model):
    ID = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=256)
    header = models.CharField(max_length=256)
    content = models.TextField()
    main_tags = models.ManyToManyField(MainTags, blank=True, null=True)
    secondary_tags = models.ManyToManyField(SecondaryTags, blank=True, null=True)
    miniature = models.ImageField(upload_to='media/miniatures/')
    main_image = models.ImageField(upload_to='media/main_images/')

class ArticleImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/gallery/', verbose_name='image')

