from django.urls import path
from . import views

app_name = "config"

urlpatterns = [
    path("", views.config_list, name="config_list"),
    path("cadastrar/", views.config_create, name="config_create"),
    
]
