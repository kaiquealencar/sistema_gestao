from django.contrib import admin
from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:cliente_id>/', views.excluir_cliente, name='excluir_cliente'),
]

