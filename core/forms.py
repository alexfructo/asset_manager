from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', max_length=32, required=True)
    password = forms.CharField(label='Senha', max_length=32, required=True, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Atenção, nome de usuário ou senha inválidos.")

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
          