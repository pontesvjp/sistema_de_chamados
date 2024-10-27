from django.db import models


class Chamado(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"Chamado [titulo={self.titulo}]"
