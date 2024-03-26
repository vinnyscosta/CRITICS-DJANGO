from django import forms
from .models import Post
from datetime import datetime

import uuid

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="User",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Vinicius Costa"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Vinicius Costa"
            }
        )
    )

    email=forms.EmailField(
        label="Email de Cadastro",
        required=True,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: vinicius.costa@exemplo.com"
            }
        )
    )

    senha_1=forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

    senha_2=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo!')
            else:
                return nome
            
    def clean_senha_2(self):
            senha_1 = self.cleaned_data.get('senha_1')
            senha_2 = self.cleaned_data.get('senha_2')
            
            if senha_1 and senha_2:
                if senha_1 != senha_2:
                    raise forms.ValidationError('Senhas não são iguais!')
                else:
                    return senha_2

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["text_post", "publicado"]

    text_post = forms.CharField(
        label="Post",
        required=True,
        max_length=200,
        widget=forms.Textarea(  
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu post aqui"
            }
        )
    )
    
    publicado = forms.BooleanField(
        label="Publicar",
        required=True,
        widget=forms.CheckboxInput(  # Corrigido para CheckboxInput
            attrs={
                "class": "form-check-input",
                "type":"checkbox",
                "role":"switch",
                "checked": True
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        text_post = cleaned_data.get("text_post")
        publicado = cleaned_data.get("publicado")

        if not text_post:
            self.add_error('text_post', 'Este campo é obrigatório.')

        return cleaned_data

    def save(self, commit=True, id_movieDB=None, type_movieDB=None, user=None):
        instance = super(PostForm, self).save(commit=False)
        instance.id_movieDB = id_movieDB
        instance.type_movieDB = type_movieDB
        instance.user = user

        while True:
            new_id = str(uuid.uuid4())[:20]
            if not Post.objects.filter(id_post=new_id).exists():
                instance.id_post = new_id
                break

        if id_movieDB and type_movieDB and user and commit:
            instance.save()

        return instance
        
