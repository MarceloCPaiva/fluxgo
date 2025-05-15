from django import forms
from .models import Solicitacao


class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ['nome', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Seu e-mail'}),
            'telefone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Seu telefone'}),
        }
