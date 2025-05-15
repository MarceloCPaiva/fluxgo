from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    Modelo que representa uma postagem de blog.
    """
    titulo = models.CharField(max_length=250)
    resumo = models.TextField(help_text="Breve resumo que aparece nos cards")
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo    


##Usuário: Paiva
##Senha: Mr140712

class Solicitacao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"
