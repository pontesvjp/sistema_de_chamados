from django.shortcuts import render
from chamados.models import Chamado


def index(request):
    chamados = Chamado.objects.all()

    return render(request, 'chamados/index.html', {"cards": chamados})


def novo_chamado(request):
    return render(request, 'chamados/novo_chamado.html')
