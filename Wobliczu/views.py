from django.shortcuts import render
from .forms import AddArticleForm, AddArticleImagesForm, AddCommentForm
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from .models import ArticleImages, Article, ArticleUser, Comment
from django.db import connection
from django.core.exceptions import ValidationError
from django.conf import settings
import requests
import json

# Create your views here.

def renderHome(request):
    context = {
        'articles': Article.objects.all().order_by('-pub_date'),
        'latest_article': Article.objects.last()
    }
    return render(request, 'main.html', context)

def renderKontakt(request):
    return render(request, 'kontakt.html')

def renderInfo(request):
    return render(request, 'search.html')

def renderArticles(request):
    context = {
        'articles': Article.objects.all().order_by('-pub_date')
    }
    return render(request, 'articles.html',context)

def renderPostCreator(request):
    if request.user.is_superuser:
        ArticleImagesFormSet = modelformset_factory(ArticleImages, form=AddArticleImagesForm, extra=6)
        if request.method == 'POST':
            us = request.user
            ruser_id = us.id
            ruser = ArticleUser.objects.get(user_id=ruser_id)
            articleForm = AddArticleForm(request.POST, request.FILES)
            articleImagesFormset = ArticleImagesFormSet(request.POST, request.FILES,
            queryset=ArticleImages.objects.none())
            if articleForm.is_valid() and articleImagesFormset.is_valid():
                article_form = articleForm.save(commit=False)
                us = request.user
                ruser_id = us.id
                ruser = ArticleUser.objects.get(user_id=ruser_id)
                ruser.numberOfArticles += 1
                ruser.add_latest_pub_date()
                ruser.save()
                article_form.user = ruser
                article_form.save()
                articleForm.save()
                articleForm.save_m2m()
                for arForm in articleImagesFormset.cleaned_data:
                    if arForm:
                        image = arForm['image']
                        articlePhoto = ArticleImages(article=article_form, image=image)
                        articlePhoto.save()
                return HttpResponseRedirect('../')
            else:
                print(articleForm.errors, articleImagesFormset.errors)
        else:
            articleForm = AddArticleForm()
            articleImagesFormset = ArticleImagesFormSet(queryset=ArticleImages.objects.none())
        context = {
            'articleForm': articleForm,
            'articleImagesFormSet': articleImagesFormset
        }
        return render(request, 'journalist/postCreator.html', context)
    else:
        return HttpResponseRedirect('accounts/login/')

def renderBase(request):
    return render(request, 'base.html')

def renderUserPanel(request):
    user = request.user
    ruser_id = user.id
    arUser = ArticleUser.objects.get(user_id=ruser_id)
    articles = Article.objects.filter(user_id=ruser_id)
    total_views = 0
    for article in articles:
        total_views += article.views
    print(len(articles))

    context = {
        'user': arUser,
        'Articles': Article.objects.all()
    }
    return render(request, 'journalist/userPanel.html', context)


def renderUserArticles(request):
    user_id = request.user.id

    context = {
        'articles': Article.objects.filter(user_id=user_id).order_by('-pub_date')
    }
    return render(request, 'journalist/userArticles.html', context)


def renderSingleArticle(request, slug):
    if request.method == 'POST':
        commentForm = AddCommentForm(request.POST)
        print('j')
        if commentForm.is_valid():
            print('d')
            comment = commentForm.save(commit=False)
            comment.article = Article.objects.get(slug=slug)
            articleCom = comment.article
            print('psa')
            link = '/articles/' + slug
            clientKey = request.POST['g-recaptcha-response']
            secretKey = '6LfSBvYUAAAAANGvFfdFTLQ_AWjUoHIMAWTsMaKO'
            captchaData = {
                'secret': secretKey,
                'response': clientKey
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
            response = json.loads(r.text)
            verify = response['success']
            print('Your success is: ', verify)
            if verify:
                commentForm.save()
                comment.save()
            return HttpResponseRedirect(link)
    else:
        articleCom = Article.objects.get(slug=slug)
        articleCom.views += 1
        articleCom.save()
        commentForm = AddCommentForm()
    context = {
        'object': Article.objects.get(slug=slug),
        'commentForm': commentForm,
        'comments': Comment.objects.filter(article=Article.objects.get(slug=slug)),
        'site_key': settings.RECAPTCHA_PUBLIC_KEY
    }
    return render(request, 'articles/article.html', context)
