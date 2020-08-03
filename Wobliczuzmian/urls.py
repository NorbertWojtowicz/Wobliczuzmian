"""Wobliczuzmian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from Wobliczu.views import renderHome, renderSearch, renderKontakt, renderPostCreator, renderBase, renderUserPanel, \
    renderArticles, renderUserArticles, renderSingleArticle, renderSearchResult, renderEditArticle, renderJournalistComments
from django.conf.urls.static import static
from django.conf import settings
from Wobliczu.models import Article


urlpatterns = [
    path('nihhal/', admin.site.urls),
    path('', renderHome, name='home'),
    path('kontakt', renderKontakt, name='kontakt'),
    path('articles/search', renderSearch, name='search'),
    path('articles', renderArticles, name='articles'),
    path('journalist/postCreator', renderPostCreator, name='postCreator'),
    path('base', renderBase, name='base'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('journalist/userPanel', renderUserPanel, name='user-panel'),
    path('journalist/userArticles', renderUserArticles, name='user-articles'),
    path('articles/<slug:slug>', renderSingleArticle, name='single-article'),
    url(r'^search-result', renderSearchResult, name='search-result'),
    path('journalist/editArticle/<slug:slug>', renderEditArticle, name='render-edit'),
    path('journalist/userPanel/<int:journalist_id>', renderJournalistComments, name='journalist-comments'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

