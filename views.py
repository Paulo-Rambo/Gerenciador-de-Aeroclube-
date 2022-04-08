from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContatoForm
from .models import Perfil, AgendamentoInstancia, UsuarioModelForm, Aula, Aeronave, Cidades
from django.views.generic import ListView, DetailView    # Importa a classe genérica ListView e DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin   # redireciona usuarios não autenticados na class-based views
from django import forms

from django.urls import reverse_lazy
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import authenticate, login, logout     # para login(da classe admin)
# from django.contrib.auth.forms import AuthenticationForm        # para login(da classe admin)
# from django.contrib.auth.models import AnonymousUser
# from django.utils.decorators import method_decorator


@login_required(login_url='login_page', redirect_field_name='acesso_negado')
def index(request):
    conteudo = "inicio.html"
    context = {
        "conteudo": conteudo,

    }
    return render(request, 'index.html')



def negado(request):
    return render(request, 'acesso_negado.html')


@login_required(login_url='login_page', redirect_field_name='acesso_negado')
def inicio(request):
    context = {

    }
    return render(request, 'inicio.html')


@login_required(login_url='login_page', redirect_field_name='acesso_negado')
def perfil(request):
    print(f'Usuário: {request.user}')
    print(f'Usuário: {request.user.id}')
    conteudo = "/perfil.html"
    numero = request.user.id
    perfil = Perfil.objects.filter(perfilNick_id=int(numero))
    # return Usuario.objects.filter(nick_key=self.request.user).order_by('due_back')
    context = {
        'perfil2': perfil,
        'conteudo': conteudo,
    }
    return render(request, 'perfil.html', context)


# from django.core import serializers
# from pyquery import PyQuery as pq

def contato(request):


    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        coisa = form.__getitem__('nome')
        #  print(f"NAMEEEEE=======> {coisa}")
        print(form)
        print(coisa)

        if form.is_valid():
            form.send_email()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Ocorreu um erro ao enviar.')

    context = {
        'form': form,
    }
    return render(request, 'contato.html', context)

from django.contrib.auth.models import User
@login_required(login_url='login_page', redirect_field_name='acesso_negado')
def usuario_view(request):
    print(f'Usuário id: {request.user.id}')
    apelido = request.user
             #print(f' Nickname : {apelido}')

    if Perfil.objects.filter(perfilNick=apelido):
        perfil = Perfil.objects.filter(perfilNick=apelido)

        context = {
            'perfil': perfil
        }
        return render(request, 'perfil.html', context)


            #print("O cadastro foi encontrado")

    if str(request.method) == 'POST':

        form = UsuarioModelForm(request.POST, request.FILES)

        if form.is_valid():

            if Perfil.objects.filter(perfilNick_id=request.user.id):
                messages.error(request, 'Você já possui cadastro de perfil!')

            else:
                form.save()
                messages.success(request, 'Perfil salvo com sucesso.')
                form = UsuarioModelForm()
        else:
            messages.error(request, 'Erro ao salvar.')
    else:
        form = UsuarioModelForm()
    context = {
        'form': form
    }
    return render(request, 'usuario.html', context)


# from django.core.paginator import Paginator
class AgendamentoListView(LoginRequiredMixin, ListView):
    paginate_by = 5
    context_object_name = 'agendamentos_lista'  # nome do objeto do contexto que será enviado para ler na template (ListView)
    template_name = 'agendamentos.html'         # nome da template onde carregará a view (ListView)
    login_url = 'login_page'                    # redireciona para página de login(LoginRequiredMixin)
    redirect_field_name = 'acesso_negado'       # (LoginRequiredMixin)
    conteudo = "agendamentos.html"

    extra_context = {
        'conteudo': conteudo,
                     }

    def get_queryset(self):
        object_list = AgendamentoInstancia.objects.filter(agendamentoPerfil__perfilNick_id=self.request.user).order_by('-criado')
        return object_list


class AgendamentoListDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'agendamentos_detalhes'
    model = AgendamentoInstancia
    login_url = 'login_page'                    # (LoginRequiredMixin)
    redirect_field_name = 'acesso_negado'       # (LoginRequiredMixin)
    template_name = 'agendamentos_detalhes.html'


class AgendamentoCreateView(LoginRequiredMixin, CreateView):

    model = AgendamentoInstancia

    escolhas = User.objects.filter(groups__name='instrutores')
    conteudo = "agendar.html"


    fields = ['agendamentoInstrutor1', 'agendamentoInstrutor2', 'agendamentoAeronave',
              'agendamentoBaseAerea', 'agendamentoAulas', 'agendamentoObservacoes', 'agendamentoData',
              'agendamentoHorario']


    extra_context = {'escolhas': escolhas,
                     'perfil': perfil,
                     'conteudo': conteudo
                     }

    template_name = 'agendar.html'
    context_object_name = "AgendamentoInstancia"

    def form_valid(self, form):
        perfil = Perfil.objects.get(perfilNick=self.request.user.id)
        form.instance.agendamentoPerfil = perfil
        return super().form_valid(form)

def aulas(request):
    return render(request, 'aulas.html')






