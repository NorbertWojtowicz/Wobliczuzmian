from django.shortcuts import render
from .forms import AddArticleForm, AddArticleImagesForm, AddCommentForm
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from .models import ArticleImages, Article, ArticleUser, Comment, MainTags, SecondaryTags
from django.db import connection
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db.models import Q
import requests
import json
from django.utils import timezone
from django.db.models import Count
from functools import reduce
from django.contrib import messages
from django.views.generic.list import ListView

# Create your views here.

def renderHome(request):
    articles = Article.objects.all().order_by('-pub_date')
    time_now = timezone.now()
    for article in articles:
        if article.when_to_public > time_now:
            articles = articles.exclude(ID=article.ID)
            print('Oj ty sobie jeszcze poczekasz..', article.ID)
    first_obj = articles.first()
    articles = articles.exclude(ID=first_obj.ID)

    context = {
        'articles': articles,
        'latest_article': first_obj
    }
    return render(request, 'main.html', context)

def renderKontakt(request):
    return render(request, 'kontakt.html')


def renderArticles(request):
    return renderArticlesListView.as_view()(request)

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
                        messages.success(request, 'Pomyślnie dodano artykuł!')
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
        return HttpResponseRedirect('../accounts/login/')


def renderBase(request):
    context = {
        'user': request.user,
    }
    return render(request, 'base.html', context)


def renderUserPanel(request):
    if request.user.is_superuser:
        user = request.user
        ruser_id = user.id
        arUser = ArticleUser.objects.get(user_id=ruser_id)
        articles = Article.objects.filter(user_id=ruser_id)
        comments = []
        numberOfComments = 0
        for article in articles:
            commentsqs = Comment.objects.filter(article=article)
            numberOfComments = numberOfComments + len(commentsqs)
        total_views = 0
        for article in articles:
            total_views += article.views
        arUser.total_views = total_views

        context = {
            'user': arUser,
            'Articles': Article.objects.all(),
            'journalist_id': ruser_id,
            'numberOfComments': numberOfComments,
        }
        return render(request, 'journalist/userPanel.html', context)
    else:
        return HttpResponseRedirect('../accounts/login/')

def renderUserArticles(request):
    if request.user.is_superuser:
        user_id = request.user.id

        context = {
            'articles': Article.objects.filter(user_id=user_id)
        }
        return renderJournalistArticlesListView.as_view()(request)
    else:
        return HttpResponseRedirect('../accounts/login/')


def renderSingleArticle(request, slug):
    if request.method == 'POST':
        try:
            if_delete = int(request.POST.get('delete'))
        except:
            if_delete = None
        if if_delete:
            comment_id = int(request.POST.get('comment_id'))
            parent_id = int(request.POST.get('parent_id'))
            if comment_id and parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                parent_obj.number_of_replies -= 1
                parent_obj.save()
                comment_obj = Comment.objects.get(id=comment_id)
                comment_obj.delete()
                link = '/articles/' + slug
                print('Deleting comment... Actual number of comments: ', parent_obj.number_of_replies)
                return HttpResponseRedirect(link)
        commentForm = AddCommentForm(request.POST)
        try:
            comment_id = int(request.POST.get('comment_id'))
        except:
            comment_id = None
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.article = Article.objects.get(slug=slug)
            if request.user.is_superuser:
                comment.username = request.user.first_name + " " + request.user.last_name
                comment.is_journalist = True
            if comment_id:
                comment_qs = Comment.objects.get(id=comment_id)
                if comment_qs:
                    reply_comment = commentForm.save(commit=False)
                    reply_comment.reply = comment_qs
                    print('Comment added... Actual number of replies: ', comment_qs.number_of_replies)
            articleCom = comment.article
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
                if comment_id:
                    comment_qs = Comment.objects.get(id=comment_id)
                    if comment_qs:
                        comment_qs.number_of_replies += 1
                        comment_qs.save()
                commentForm.save()
                comment.save()
                messages.success(request, 'Komentarz został pomyślnie dodany!')
            else:
                messages.error(request, 'Nie udało się dodać komentarza, musisz potwierdzić, że nie jesteś robotem!')
            context = {
                'object': Article.objects.get(slug=slug),
                'comments': Comment.objects.filter(article=Article.objects.get(slug=slug)),
                'site_key': settings.RECAPTCHA_PUBLIC_KEY,
                'commentForm': AddCommentForm(),
                'user': request.user,
            }
            return HttpResponseRedirect(link)

    else:
        articleCom = Article.objects.get(slug=slug)
        articleCom.views += 1
        articleCom.save()
        commentForm = AddCommentForm()
    context = {
        'object': Article.objects.get(slug=slug),
        'comments': Comment.objects.filter(article=Article.objects.get(slug=slug)),
        'site_key': settings.RECAPTCHA_PUBLIC_KEY,
        'commentForm': AddCommentForm(),
        'user': request.user,
    }
    return render(request, 'articles/article.html', context)

def renderSearch(request):
    if request.method == 'POST':
        return renderSearchResult(request)
    context = {
        'mainTags': MainTags.objects.all(),
        'secondaryTags': SecondaryTags.objects.all(),
    }
    return render(request, "search.html", context)

def renderSearchResult(request):
    geoTags = []
    categoryTags = []
    catTagsId = []
    titles = []
    jakas = []
    errors = []
    time_now = timezone.now()
    for mTag in MainTags.objects.all():
        if request.POST.get(mTag.main_tag) is not None:
            geoTags.append(request.POST.get(mTag.main_tag))
            #print(tab)
    if len(geoTags) > 1:
        errors.append('Możesz wybrać maksymalnie jeden region!')
    if len(geoTags) < 1:
        errors.append('Musisz wybrać region!')
    if errors:
        context = {
            'mainTags': MainTags.objects.all(),
            'secondaryTags': SecondaryTags.objects.all(),
            'errors': errors
        }
        return render(request, 'search.html', context)
    for sTag in SecondaryTags.objects.all():
        if request.POST.get(sTag.secondary_tag) is not None:
            categoryTags.append(request.POST.get(sTag.secondary_tag))
            #print(tabSecond)
    geoTagId = MainTags.objects.get(main_tag=geoTags[0])
    print(geoTagId.id)
    query = Q(main_tags=geoTagId.id)
    for categoryTag in categoryTags:
        catTagsId.append(SecondaryTags.objects.get(secondary_tag=categoryTag))
    #articles = Article.objects.filter(queries[0] & queries[1])
    for id in catTagsId:
        jakas.append(id.id)
    tytul = 'jd'
    print(catTagsId)
    number_of_tags = len(catTagsId)
    objects_ext = Article.objects.filter(main_tags=geoTagId)
    for i in catTagsId:
        objects_ext = objects_ext.filter(secondary_tags=i)
    for obj in objects_ext:
        titles = obj.title
    rest_of_articles = Article.objects.filter(reduce(lambda x, y : x | y,(Q(secondary_tags=idd) for idd in catTagsId)))\
        .distinct()
    #rest_of_articles.exclude(secondary_tags__secondary_tags__in=objects_ext)
    print(rest_of_articles)
    context = {
        'obj': objects_ext.exclude(when_to_public__gt=time_now),
        'rest': rest_of_articles.exclude(when_to_public__gt=time_now)
    }

    return render(request, 'searchResult.html', context)


def renderEditArticle(request, id):
    if request.user.is_superuser:
        instance = Article.objects.get(ID=id)
        form = AddArticleForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('postCreator')
        return render(request, 'journalist/editArticle.html', {'articleForm': form})
    else:
        return HttpResponseRedirect('../../accounts/login/')


class renderArticlesListView(ListView):
    time_now = timezone.now()
    articles = Article.objects.all().exclude(when_to_public__gt=time_now).order_by('-pub_date')
    print(articles)
    queryset = articles
    paginate_by = 2


class renderJournalistArticlesListView(ListView):
    user = None
    paginate_by = 2
    context_object_name = 'articles'
    template_name = 'journalist/userArticles.html'

    def get_context_data(self, **kwargs):
        print(self.user)
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.now()
        return context

    def get_queryset(self):
        queryset = super(renderJournalistArticlesListView, self).get_queryset()
        queryset = Article.objects.filter(user_id=self.request.user.id).order_by('-pub_date')
        return queryset
    queryset = get_queryset


def renderJournalistComments(request, journalist_id):
    journalist = ArticleUser.objects.get()
