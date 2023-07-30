from django.contrib import admin

#importando todas as classes do aplicativo
from app_agenda.models import *

#tratamento para visualização das classes na pagina em questão
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'data_criacao')
    list_filter = ('titulo', 'descricao', 'data', 'data_criacao', 'usuario')

# Register your models here.
admin.site.register(Evento, EventoAdmin)
