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

]