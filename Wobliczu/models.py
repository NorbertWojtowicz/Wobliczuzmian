from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
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
        self.last_pub_date = timezone.localtime(timezone.now())


    def __str__(self):
        name = self.user.first_name + " " + self.user.last_name
        return name


class Article(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(ArticleUser, on_delete=models.CASCADE, null=True, blank=True, related_name='users')
    title = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    short_desc = models.CharField(max_length=650)
    content = RichTextUploadingField(blank=True, null=True, config_name='rich_config')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    main_tags = models.ManyToManyField(MainTags, null=True)
    secondary_tags = models.ManyToManyField(SecondaryTags, null=True)
    miniature = models.ImageField(upload_to='media/miniatures/')
    main_image = models.ImageField(upload_to='media/main_images/')
    when_to_public = models.DateTimeField(default=timezone.now, blank=True)

    def delete(self, **kwargs):
        print('Usuwam artykuł id: ', self.id, ' o tytule: ', self.title)
        self.user.numberOfArticles -= 1
        self.user.save()
        super(Article, self).delete()

    def get_absolute_url(self):
        return reverse('Wobliczu:renderSingleArticle', kwargs={"id": self.id})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")


        
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Article)


class ArticleImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/gallery/', verbose_name='image')


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    username = models.CharField(max_length=30, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.CharField(max_length=999, null=True)
    number_of_replies = models.IntegerField(blank=True, default=0)
    is_journalist = models.BooleanField(max_length=5, default=False)

