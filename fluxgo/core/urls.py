from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, ServicosView, ContatoServiceView, BlogView, PostListView, PostDetailView, SolicitacaoServicoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('servicos/', ServicosView.as_view(), name='servicos'), 
    path('contato-servico/', ContatoServiceView.as_view(), name='contato_servico'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('solicitar/', SolicitacaoServicoView.as_view(), name='solicitar_servico'),
    path('obrigado/', TemplateView.as_view(template_name='core/solicitacao_sucesso.html'), name='solicitacao_sucesso')
]