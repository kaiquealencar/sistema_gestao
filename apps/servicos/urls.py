from django.urls import path
from . import views

app_name = "servicos"

urlpatterns = [
    path("", views.servico_list, name='servico_list'),
    path("novo/", views.servico_create, name='servico_create'),
    path("editar/<int:servico_id>/", views.servico_edit, name='servico_edit'),
    path("excluir/<int:servico_id>/", views.servico_delete, name='servico_delete'),   
]
