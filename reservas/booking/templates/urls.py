from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_reservas, name='listar_reservas'),
    path('criar/', views.criar_reserva, name='criar_reserva'),
    path('confirmar/<int:reserva_id>/', views.confirmar_chegada, name='confirmar_chegada'),
    path('editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
    path('deletar/<int:reserva_id>/', views.deletar_reserva, name='deletar_reserva'),
]