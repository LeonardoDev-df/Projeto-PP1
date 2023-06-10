from django.contrib import admin
from django.urls import path
from booking.views import listar_reservas, criar_reserva, confirmar_chegada, cancelar_reserva, editar_reserva, deletar_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_reservas, name='listar_reservas'),
    path('reservas/criar/', criar_reserva, name='criar_reserva'),
    path('reservas/confirmar-chegada/<int:reserva_id>/', confirmar_chegada, name='confirmar_chegada'),
    path('reservas/cancelar-reserva/<int:reserva_id>/', cancelar_reserva, name='cancelar_reserva'),
    path('reservas/editar/<int:reserva_id>/', editar_reserva, name='editar_reserva'),
    path('reservas/deletar/<int:pk>/', deletar_reserva, name='deletar_reserva'),
]
