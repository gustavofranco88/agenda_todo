from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(verbose_name='Data')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Criado em')

    class Meta:
        ''' aqui estou forçando o nome da tabela como 'evento' '''
        db_table = 'evento'
