from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django import forms
from .models import Post

class HomeView(TemplateView):
    """
    View para exibir a página inicial do site FluxGo
    """
    template_name = 'core/home.html'
    

class ServicosView(TemplateView):
    """
    View para exibir a página de serviços oferecidos pela FluxGo.
    """
    template_name = 'core/servicos.html'


class BlogView(ListView):
    """
    View baseada em classe que exibe a lista de posts do blog.
    """
    template_name = 'core/blog.html'
    model = Post
    context_object_name = 'posts'
    

class ContatoServicoForm(forms.Form):
    """
    Formulário para o cliente preencher seus dados ao solicitar um serviço.
    Inclui os campos: nome, email, whatsapp e tipo de serviço (oculto).
    """
    nome = forms.CharField(label='Nome', max_length=150)
    email = forms.EmailField(label='Email')
    telefone = forms.CharField(label='Telefone', max_length=20)
    tipo = forms.CharField(widget=forms.HiddenInput())
    

class ContatoServiceView(FormView):
    """
    View baseada em formulário para solicitar um serviço específico.
    Mostra o formulário e processa os dados ao ser submetido.
    """
    template_name = "core/contato_servico.html"
    form_class = ContatoServicoForm
    success_url = reverse_lazy('home')
    
    def get_initial(self):
        """
        Preenche o campo oculto 'tipo' com base no parâmetro de query string da URL.
        """
        initial = super().get_initial()
        initial['tipo'] = self.request.GET.get('tipo', '')
        return initial
    
    def form_valid(self, form):
        """
        Trata o formulário quando os dados são válidos. Aqui pode ser adicionado
        lógica para salvar os dados ou enviar um e-mail.
        """
        print("Dados recebidos:", form.cleaned_data)
        return super().form_valid(form)


class PostListView(ListView):
    """
    Exibe a lista de posts no blog com cards.
    """
    model = Post
    template_name = "core/blog.html"
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """
    Exibe o conteúdo completo de um post específico.
    """
    model = Post
    template_name = "core/post_detail.html"
    context_object_name = 'post'
