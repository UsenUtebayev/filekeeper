from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from videokeeper.models import VideoModel


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользвателя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользвателя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class VideoForm(forms.ModelForm):

    class Meta:
        model = VideoModel
        fields = ('name', 'description', 'videoUrl')
