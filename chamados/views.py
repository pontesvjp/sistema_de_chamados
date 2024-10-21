from django.shortcuts import render



def index(request):
    return render(request, 'chamados/index.html')

def novo_chamado(request):
    return render(request, 'chamados/novo_chamado.html')
