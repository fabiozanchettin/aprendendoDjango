from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

# Create your views here.
def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        #print(f'Post: {request.POST}')
        if form.is_valid():
            form.send_mail()
            '''
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('mensagem enviada')
            print(f'nome: {nome}')
            print(f'email: {email}')
            print(f'assunto: {assunto}')
            print(f'mensagem: {mensagem}')
            '''
            messages.success(request, 'email enviado com sucesso')
            form = ContatoForm
        else:
            messages.error(request, 'erro ao enviar o email')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'produto salvo ok')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'erro deu pau')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)