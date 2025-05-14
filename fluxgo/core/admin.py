from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configuração de exibição do modelo Post no painel administrativo.
    """
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'resumo')
    list_filter = ('data_publicacao',)
    ordering = ('-data_publicacao',)
