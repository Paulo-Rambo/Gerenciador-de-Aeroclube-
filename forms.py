from django import forms
from django.core.mail.message import EmailMessage

from .models import AgendamentoInstancia
from django.contrib.auth.models import User
from django.db import models

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        email = EmailMessage(
            subject='Email enviado pelo app1.',
            body=conteudo,
            from_email='contato@seudominio.com',
            to=['contato@seudominio.com'],
            headers={'Reply-To': email}
        )
        email.send()


