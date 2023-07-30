from django.shortcuts import render

# Create your views here.

def lista_eventos(request):
    render(request, 'agenda.html')

