from django import forms
from .models import ArticleImages, Article, Comment, SecondaryTags, MainTags
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


ARTICLE_MAIN_TAGS = (
    ('PL', 'Polska'),
    ('AM', 'Ameryka'),
    ('SW', 'Świat'),
    ('EU', 'Europa'),
)
ARTICLE_SECONDARY_TAGS = (
    ('PLT', 'Polityka'),
    ('EKO', 'Ekonomia'),
    ('ZDR', 'Zdrowie'),
    ('WOJ', 'Wojsko'),
)


class AddArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'short_desc', 'content', 'miniature', 'main_image', 'main_tags', 'secondary_tags',
                  'user', 'slug', 'when_to_public')
        widgets = {
            'title': forms.Textarea(attrs={'class': 'input'}),
            'short_desc': forms.Textarea(attrs={'class': 'input'}),
            'miniature': forms.ClearableFileInput(attrs={'class': 'inputImage'}),
            'main_image': forms.ClearableFileInput(attrs={'class': 'inputImage'}),
            'main_tags': forms.CheckboxSelectMultiple(attrs={'class': 'checkboxMltp'}),
            'secondary_tags': forms.CheckboxSelectMultiple(attrs={'class': 'checkboxMltp'}),
            'when_to_public': forms.DateTimeInput(attrs={'class': 'input'}),
        }

class AddArticleImagesForm(forms.ModelForm):
    class Meta:
        model = ArticleImages
        fields = ('image', )
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'inputImage1'}),
        }


class AddCommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('username', 'content', 'article')
        widgets = {
            'username': forms.Textarea(attrs={'class': 'comment-add-username'}),
            'content': forms.Textarea(attrs={'class': 'comment-add-content'}),
        }


class SearchForm(forms.ModelForm):
    class Meta:
        pass


class EditArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'short_desc', 'content', 'miniature', 'main_image', 'main_tags', 'secondary_tags',
                  'user', 'slug', 'when_to_public')
