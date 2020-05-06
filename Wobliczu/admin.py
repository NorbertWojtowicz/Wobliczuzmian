from django.contrib import admin
from .models import Article, ArticleImages, MainTags, SecondaryTags, ArticleUser

# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleImages)
admin.site.register(MainTags)
admin.site.register(SecondaryTags)
admin.site.register(ArticleUser)


