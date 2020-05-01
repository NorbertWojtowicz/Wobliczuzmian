from django import forms
from .models import ArticleImages, Article

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'short_desc', 'header', 'content', 'miniature', 'main_image')
        widgets = {
            'title': forms.Textarea(attrs={'class': 'input'}),
            'short_desc': forms.Textarea(attrs={'class': 'input'}),
            'header': forms.Textarea(attrs={'class': 'input'}),
            'content': forms.Textarea(attrs={'class': 'input'}),
            'miniature': forms.ClearableFileInput(attrs={'class': 'inputImage'}),
            'main_image': forms.ClearableFileInput(attrs={'class': 'inputImage'}),
        }

class AddArticleImagesForm(forms.ModelForm):
    class Meta:
        model = ArticleImages
        fields = ('image', )
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'inputImage1'}),
        }
