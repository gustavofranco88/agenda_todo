from django.shortcuts import redirect
from django.shortcuts import render
from app_agenda.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(
            username=username,
            password=password
        )
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, message='Usuário ou senha inválido')
    return redirect('/')


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


# criar eventos
@login_required(login_url='/login/')
def novo_evento(request):
    return render(request, 'eventos.html')


@login_required(login_url='/login')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data = request.POST.get('data')
        descricao = request.POST.get('descicao')
        usuario = request.user
        # persistir dados no banco
        Evento.objects.create(
            titulo=titulo,
            data=data,
            descricao=descricao,
            usuario=usuario
        )
    return redirect('/')


# visualizar eventos
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)

# @login_required(login_url='/login/')
