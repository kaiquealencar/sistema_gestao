from django.contrib import admin
from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('cadastrar/', views.cliente_create, name='cliente_create'),
    path('<int:cliente_id>/editar/', views.cliente_edit, name='cliente_edit'),
    path('<int:cliente_id>/excluir/', views.cliente_delete, name='cliente_delete'),
]

