from django.urls import path  # include
from .views import index, contato, usuario_view, perfil, inicio, negado, aulas
from .views import AgendamentoListView, AgendamentoListDetailView, AgendamentoCreateView
from django.contrib.auth import views as auth_views

# import views

urlpatterns = [

    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('usuario/', usuario_view, name='usuario'),
    path('perfil/', perfil, name='perfil'),
    path('inicio/', inicio, name='inicio'),
                            #   path('perfil/', , name='perfil'), agora está em usuario_view
    path('aulas/', aulas, name='aulas'),
    path('agendar/', AgendamentoCreateView.as_view(), name='agendar'),
    path('agendamentos_lista/', AgendamentoListView.as_view(), name='agendamentos'),

    path('agendamentos_lista/detalhes/<str:pk>', AgendamentoListDetailView.as_view(), name='agendamentos_detalhes'),
    path('login_page/', auth_views.LoginView.as_view(template_name='autentica/login_page.html', redirect_field_name='inicio'), name='login_page'),
    path('logout_page/', auth_views.LogoutView.as_view(template_name='autentica/logout_page.html'), name='logout_page'), # https://docs.djangoproject.com/en/3.1/topics/auth/default/#using-the-views
    path('acesso_negado/', negado, name='negado')
]