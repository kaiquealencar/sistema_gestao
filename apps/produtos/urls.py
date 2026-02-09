from django.urls import path
from . import views

app_name = "produtos"

urlpatterns = [
    path("", views.produto_create, name='produto_list'),
    path("novo/", views.produto_create, name='produto_create'),
    path("<int:id>/editar/", views.produto_list, name='produto_edit'),
]
