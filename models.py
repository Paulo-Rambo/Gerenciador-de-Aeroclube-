from django.db import models
from django.db.models.functions import Coalesce  # usado para numerar os objetos AgendamentosInstancia
from django import forms
from stdimage.models import StdImageField
from django.conf import settings
from django.contrib.auth.models import User
from app1 import validadores
import uuid
from django.core import validators
from django.urls import reverse  # Usado para gerar URLs para reverter as identificações URL

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    #perfilNick = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=False)

    class Meta:
        abstract = True


class Cidades(models.Model):
    cidade = models.CharField('Cidade', max_length=50, primary_key=True)
    estado = models.CharField('Estado', max_length=50, null=True)

    def __str__(self):
        return self.cidade


class Aeronave(models.Model):
    aeronaveModelo = models.CharField('Aeronave', max_length=40, null=False)
    aeronaveIdentificacao = models.CharField('Aeronave ID', max_length=40, null=True)

    def __str__(self):
        return self.aeronaveModelo


class Perfil(Base):
    perfilNick = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    slug = models.SlugField('Slug', max_length=100, null=True, editable=False)
    imagem = StdImageField('Imagem', upload_to='perfil_headshots', variations={'thumb': (65, 65)}, null=True)
    perfilNome = models.CharField('Nome', max_length=50)
    perfilIdade = models.IntegerField('Idade', null=True)   
    perfilCidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, null=True, verbose_name="Cidade.")
    # perfilEstado = models.OneToOneField(Cidades, on_delete=models.CASCADE)
    perfilTelefoneFixo = models.DecimalField('Telefone', decimal_places=1, max_digits=12, null=True)  # validators=[validadores.validate_telefone])
    perfilTelefoneCelular = models.DecimalField('Celular', decimal_places=1, max_digits=15, null=True)  # validators=[validadores.validate_Celular])
    perfilEmail = models.EmailField('E-mail')
    perfilCPF = models.CharField('Número do CPF', max_length=11, validators=[validators.integer_validator, validadores.validate_cpf], null=True)
    perfilValidadeDoCCF = models.DateField('Data de validade do CCF', null=True)
    perfilLicenca = models.CharField('Licenças', max_length=20, null=True)
    perfilHabilitacoes = models.CharField('Habilitações', max_length=40, null=True)
    perfilMNTE = models.DateField('MNTE', null=True)

    def __str__(self):
        return self.perfilNome


def perfil_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.perfilNome)


signals.pre_save.connect(perfil_pre_save, sender=Perfil)


class Aula(models.Model):
    aulaAula = models.CharField(max_length=40, help_text=str('Coloque o nome da matéria.'), null=False, verbose_name="Aula:")
    aulaDescrição = models.TextField(verbose_name="Descrição da aula:")
    def __str__(self):
        return f'{self.aulaAula}'

class AgendamentoInstancia(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text=str('Id unico para o agendamento.'))
    agendamentoPerfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, help_text=str('Instrutor.'), related_name="Perfil", verbose_name="Perfil:")
    agendamentoInstrutor1 = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name="Instrutor 1:", related_name="instrutor_1")
    agendamentoInstrutor2 = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name="Instrutor 2:", related_name="instrutor_2")
    #agendamentoCliente = models.CharField('Cliente', max_length=40, null=False)
    agendamentoValidadeCCF = models.CharField('Validade do CCF', max_length=40)
    agendamentoData = models.DateField('Data')
    agendamentoHorario = models.TimeField('Horário:')
    agendamentoAeronave = models.ForeignKey(Aeronave, on_delete=models.CASCADE, null=False, verbose_name="Selecione a aeronave:")
    agendamentoHorasDisponiveis = models.IntegerField('Horas de voô disponíveis', null=True, blank=True)
    agendamentoNumeroDeHoras = models.FloatField('Agendar horas', null=False,)
    agendamentoBaseAerea = models.ForeignKey(Cidades, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Base aérea:",)
    agendamentoObservacoes = models.TextField('Observações', max_length=1000, null=True, blank=True)
    agendamentoAulas = models.ForeignKey(Aula, on_delete=models.CASCADE, verbose_name="Tipo de instrução.")
    AGENDAMENTO_STATUS = (
            ('e', 'Em curso.'),
            ('c', 'Cancelado!'),
            ('a', 'Atrasado.'),
            ('r', 'Reservado.'),
            ('f', 'Concluído.'),
            ('m', 'Em requisição')
        )
    agendamentoStatus = models.CharField(
        max_length=1,
        choices=AGENDAMENTO_STATUS,
        blank=True,
        default='m',
        help_text='Estado do agendamento.',
    )

    class Meta:
        ordering = ['-criado']


    def __str__(self):
        return f'{self.id}'

    def get_absolute_url(self):
        """Retorna o URL para acessar uma instância específica do modelo."""
        return reverse('agendamentos_detalhes', args=[str(self.pk)])        # manda o id do objeto para o DetailView


class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['perfilNome', 'imagem', 'perfilIdade', 'perfilCidade',
                  'perfilTelefoneFixo', 'perfilTelefoneCelular', 'perfilEmail',
                  'perfilCPF', 'perfilValidadeDoCCF', 'perfilLicenca', 'perfilHabilitacoes', 'perfilMNTE']


        app_label = 'UsuarioModelForm'

        def __str__(self):
            return self.perfilNome

