from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.CharField(label='email')
    assunto = forms.CharField(label='assunto')
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())
