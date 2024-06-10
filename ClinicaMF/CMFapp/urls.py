from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profissionais/', views.listar_profissionais, name='listar_profissionais'),
]
