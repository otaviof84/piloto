from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem vindos ao nosso site")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim mesmo.</h1>")


def contato(request):
    return HttpResponse("Página de Contato")

def ajuda(request):
    return HttpResponse("Página de Ajuda")