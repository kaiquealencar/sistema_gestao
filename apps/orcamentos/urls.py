from django.urls import path
from . import views
app_name = "orcamentos"

urlpatterns = [
    path('', views.orcamento_list, name='orcamento_list'),
    path('cadastrar/', views.orcamento_create, name='orcamento_create'),
    path('<int:id>/', views.orcamento_detail, name='orcamento_detail'),
    path('<int:id>/edit/', views.orcamento_edit, name='orcamento_edit'),
    path('<int:id>/delete/', views.orcamento_delete, name='orcamento_delete'),

]

