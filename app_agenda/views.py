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
    id_evento = request.GET.get('id')
    print(id_evento)
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
        print(dados)
    return render(request, 'eventos.html', dados)


@login_required(login_url='/login')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data = request.POST.get('data')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        print(f'esse é o id: {id_evento}')
        # persistir dados no banco
        if id_evento:
            print('Update')
            Evento.objects.filter(id=id_evento).update(
                titulo=titulo,
                data=data,
                descricao=descricao,
                usuario=usuario
            )
        else:
            print('criando')
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

# atualizar eventos

# deletar eventos
@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects .get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')


# @login_required(login_url='/login/')
