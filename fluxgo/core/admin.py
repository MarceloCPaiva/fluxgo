from django.contrib import admin
from .models import Post, Solicitacao

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configuração de exibição do modelo Post no painel administrativo.
    """
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'resumo')
    list_filter = ('data_publicacao',)
    ordering = ('-data_publicacao',)


@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    """
    Exibe as solicitações de serviço no admin.
    """
    list_display = ('nome', 'email', 'telefone', 'data_criacao')
    search_fields = ('nome', 'email', 'telefone')
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)
