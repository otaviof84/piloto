from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


produtos_lista = [
    {'id': 1, 'nome': 'Notebook', 'preco': '2500,00'},
    {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
    {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
]

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def produtos(request):
    return render(request, 'produto/lista.html', {
        'lista': produtos_lista
    })

def detalhes_produto(request, id):
    produto = next((p for p in produtos_lista if p['id'] == id), None)
    return render(request, 'produto/detalhes.html', {'produto': produto})

def adicionar_produto(request):
    if request.method == 'POST':
        novo_id = len(produtos_lista) + 1
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        produtos_lista.append({
            'id': novo_id,
            'nome': nome,
            'preco': preco
        })
        messages.success(request, 'Produto adicionado com sucesso!')
        return redirect('produtos')

        return redirect('produtos')

    return render(request, 'produto/formulario.html')

def editar_produto(request, id):
    produto = next((p for p in produtos_lista if p['id'] == id), None)

    if request.method == 'POST':
        produto['nome'] = request.POST.get('nome')
        produto['preco'] = request.POST.get('preco')
        return redirect('produtos')

    return render(request, 'produto/formulario.html', {'produto': produto})

def excluir_produto(request, id):
    produto = next((p for p in produtos_lista if p['id'] == id), None)

    if request.method == 'POST':
        produtos_lista.remove(produto)
        return redirect('produtos')

    return render(request, 'produto/excluir.html', {'produto': produto})


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




