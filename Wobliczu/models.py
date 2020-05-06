from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.

class MainTags(models.Model):
    main_tag = models.CharField(max_length=20)
    def __str__(self):
        return self.main_tag


class SecondaryTags(models.Model):
    secondary_tag = models.CharField(max_length=20)

    def __str__(self):
        return self.secondary_tag


class ArticleUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numberOfArticles = models.IntegerField(verbose_name='numberOfArticles')
    last_pub_date = models.DateTimeField(default=datetime.now())
    total_views = models.IntegerField(default=0)

    def add_article(self):
        self.numberOfArticles += 1
        return self.numberOfArticles

    def remove_article(self):
        self.numberOfArticles -= 1

    def add_latest_pub_date(self):
        pass


    def __str__(self):
        return self.user.first_name


class Article(models.Model):
    ID = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(ArticleUser, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    short_desc = models.CharField(max_length=256)
    header = models.CharField(max_length=256)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    main_tags = models.ManyToManyField(MainTags, blank=True, null=True)
    secondary_tags = models.ManyToManyField(SecondaryTags, blank=True, null=True)
    miniature = models.ImageField(upload_to='media/miniatures/')
    main_image = models.ImageField(upload_to='media/main_images/')
    def delete(self, **kwargs):
        print('Usuwam artykuł id: ', self.ID, ' o tytule: ', self.title)
        self.user.numberOfArticles -= 1
        self.user.save()
        super(Article, self).delete()

class ArticleImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/gallery/', verbose_name='image')

