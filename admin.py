from django.contrib import admin

from .models import Perfil, Cidades, Aeronave, Aula, AgendamentoInstancia


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('perfilNome', 'perfilCidade', 'perfilTelefoneFixo', 'imagem', 'slug', 'criado', 'modificado', 'ativo')


@admin.register(Cidades)
class CidadeslAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'estado')


@admin.register(Aeronave)
class AeronaveAdmin(admin.ModelAdmin):
    list_display = ('aeronaveModelo', 'aeronaveIdentificacao')


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('aulaAula',)

@admin.register(AgendamentoInstancia)
class AgendamentoInstanciaAdmin(admin.ModelAdmin):
    list_display = ('agendamentoInstrutor1', 'agendamentoBaseAerea')