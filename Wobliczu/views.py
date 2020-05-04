from django.shortcuts import render
from .forms import AddArticleForm, AddArticleImagesForm
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from .models import ArticleImages, Article
from django.core.exceptions import ValidationError

# Create your views here.

def renderHome(request):
    context = {
        'article': Article.objects.all()
    }
    return render(request, 'main.html', context)

def renderKontakt(request):
    return render(request, 'kontakt.html')

def renderInfo(request):
    return render(request, 'o_nas.html')

def renderPostCreator(request):
    if request.user.is_superuser:
        ArticleImagesFormSet = modelformset_factory(ArticleImages, form=AddArticleImagesForm, extra=6)
        if request.method == 'POST':
            articleForm = AddArticleForm(request.POST, request.FILES)
            articleImagesFormset = ArticleImagesFormSet(request.POST, request.FILES,
            queryset=ArticleImages.objects.none())
            print('chuj')
            if articleForm.is_valid() and articleImagesFormset.is_valid():
                print('przeszlo')
                article_form = articleForm.save(commit=False)
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
        return render(request, 'postCreator.html', context)
    else:
        return HttpResponseRedirect('accounts/login/')

def renderBase(request):
    return render(request, 'base.html')