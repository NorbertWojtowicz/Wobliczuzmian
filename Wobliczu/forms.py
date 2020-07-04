from django import forms
from .models import ArticleImages, Article, Comment, SecondaryTags, MainTags


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
                  'user', 'image_section_two', 'text_section_two', 'image_section_three', 'text_section_three',
                  'image_section_four', 'text_section_four', 'slug', 'when_to_public')
        widgets = {
            'title': forms.Textarea(attrs={'class': 'input'}),
            'short_desc': forms.Textarea(attrs={'class': 'input'}),
            'content': forms.Textarea(attrs={'class': 'input'}),
            'miniature': forms.ClearableFileInput(attrs={'class': 'inputImage'}),
            'main_image': forms.ClearableFileInput(attrs={'class': 'inputImage'}),
            'image_section_two': forms.ClearableFileInput(attrs={'class': 'inputImage'}),
            'image_section_three': forms.ClearableFileInput(attrs={'class': 'inputImage'}),
            'image_section_four': forms.ClearableFileInput(attrs={'class': 'inputImage'}),
            'text_section_two': forms.Textarea(attrs={'class': 'input'}),
            'text_section_three': forms.Textarea(attrs={'class': 'input'}),
            'text_section_four': forms.Textarea(attrs={'class': 'input'}),
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
            'username': forms.Textarea(attrs={'class': 'commentUsername', 'placeholder': 'Pseudonim'}),
            'content': forms.Textarea(attrs={'class': 'commentContent', 'placeholder': 'Komentarz'}),
        }


class SearchForm(forms.ModelForm):
    class Meta:
        pass
