from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.CharField(label='email')
    assunto = forms.CharField(label='assunto')
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'nome: {nome}\nE-mail:{email}\nassunto:{assunto}\nmensagem:{mensagem}\n'

        mail = EmailMessage(
            subject='Email pelo Django',
            body=conteudo,
            from_email='fabiozan@gmail.com',
            to=['contato@contato', 'outro@outro'],
            headers={'Reply-to': email}
        )
        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']