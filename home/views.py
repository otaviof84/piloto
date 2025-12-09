from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def produtos(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
        ],
    }
    return render(request, 'produto/lista.html', contexto)

def exibir_item(request, id):
    return HttpResponse(f"Você pediu para exibir o item {id}")

def diasemana(request, num):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }

    nome = dias.get(num, "Dia inválido")
    return HttpResponse(f"Dia escolhido: {nome}")

