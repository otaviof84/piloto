from django.http import HttpResponse

def index(request):
    return HttpResponse("A view index  funcionou, wow!")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim mesmo.</h1>")