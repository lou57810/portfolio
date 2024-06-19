from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'role']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63) #, label='Email')
    password = forms.CharField(max_length=63) #, widget=forms.PasswordInput, label='Mot de passe')


class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['profile_photo']
