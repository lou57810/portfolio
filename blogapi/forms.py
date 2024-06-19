from django import forms

from . import models


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.MementoItems
        fields = ['item_name', 'item_explanation']


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=60, label='Titre')
    # image = forms.ImageField(required=False)

    class Meta:
        model = models.Article
        # fields = ['title', 'description', 'image']
        fields = ['title', 'description']