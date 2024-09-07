from django import forms

from . import models


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']


class CardForm(forms.ModelForm):
    display_card = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Card
        fields = ['title', 'content']


class DeleteCardForm(forms.Form):
    delete_card = forms.BooleanField(widget=forms.HiddenInput, initial=True)


# MEMENTO
class ItemForm(forms.ModelForm):
    class Meta:
        model = models.MementoItems
        fields = ['item_name', 'item_explanation']


# ARTICLE
class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'description', 'user', 'image']
