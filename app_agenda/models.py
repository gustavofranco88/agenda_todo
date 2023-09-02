from django.db import models
from django.contrib.auth.models import User #importando classes do django admin

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(verbose_name='Data')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Criado em')
    #criando uma foreignkey da classe django-admin
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #on_delete=models.CASCADE é obrigatorio, caso um usuario seja deletado, todos os eventos dele serão tbm
    

    class Meta:
        ''' aqui estou forçando o nome da tabela como 'evento' '''
        db_table = 'evento'

    def __str__(self):
        return self.titulo
