from django.urls import path
from .views import HomeView, ServicosView, ContatoServiceView, BlogView, PostListView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('servicos/', ServicosView.as_view(), name='servicos'), 
    path('contato-servico/', ContatoServiceView.as_view(), name='contato_servico'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail')
]