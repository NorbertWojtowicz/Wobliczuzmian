from django.shortcuts import render
from .forms import AddArticleForm, AddArticleImagesForm
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from .models import ArticleImages, Article

# Create your views here.

def renderHome(request):
    return render(request, 'main.html')

def renderKontakt(request):
    return render(request, 'kontakt.html')

def renderInfo(request):
    return render(request, 'o_nas.html')

def renderPostCreator(request):
    ArticleImagesFormSet = modelformset_factory(ArticleImages, form=AddArticleImagesForm, extra=6)
    if request.method == 'POST':
        articleForm = AddArticleForm(request.POST, request.FILES)
        articleImagesFormset = ArticleImagesFormSet(request.POST, request.FILES,
        queryset=ArticleImages.objects.none())
        if articleForm.is_valid() and articleImagesFormset.is_valid():
            article_form = articleForm.save(commit=False)
            articleForm.save()
            for arForm in articleImagesFormset.cleaned_data:
                image = arForm['image']
                articlePhoto = ArticleImages(article=article_form, image=image)
                articlePhoto.save()
            return HttpResponseRedirect('')
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

def renderBase(request):
    return render(request, 'base.html')