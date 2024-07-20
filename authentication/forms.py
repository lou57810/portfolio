from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()  # Nécéssaire pour l'implémentation du logging avec email et valeur dans settings.


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()  # Nécéssaire à l'implémentation du logging avec email et la valeur dans settings.
        # model = User
        fields = ['first_name', 'email']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=64)  # , label='Email')
    password = forms.CharField(max_length=64)  # , widget=forms.PasswordInput, label='Mot de passe')


class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['profile_photo']
