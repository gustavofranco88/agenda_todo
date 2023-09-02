from django.shortcuts import render
from app_agenda.models import Evento
# Create your views here.

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)

