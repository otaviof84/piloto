from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"), 
    path('ajuda/', views.ajuda, name="ajuda"),
    path('produtos/', views.produtos, name="produtos"),
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('dia/<int:num>/', views.diasemana, name='diasemana'),
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/detalhes/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),

]