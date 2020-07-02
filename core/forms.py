from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Localizacao, Setor, Grupo, Categoria, Fabricante, Equipamento


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nome de usuário', max_length=32, required=True)
    password = forms.CharField(
        label='Senha', max_length=32, required=True, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Atenção, nome de usuário ou senha inválidos.")

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = '__all__'
        widgets = {
            'observacoes': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'codigo': 'Código',
            'localizacao': 'Unidade',
            'grupo': 'Localização',
            'numero_serie': 'Nº de Série',
            'numero_patrimonio': 'Nº de Patrimônio',
            'observacoes': 'Observações',
        }
