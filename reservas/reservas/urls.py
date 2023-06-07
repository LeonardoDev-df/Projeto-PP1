from django.contrib import admin
from django.urls import path
from booking.views import listar_reservas, criar_reserva, editar_reserva, deletar_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_reservas, name='listar_reservas'),
    path('reservas/criar/', criar_reserva, name='criar_reserva'),
    path('reservas/editar/<int:pk>/', editar_reserva, name='editar_reserva'),
    path('reservas/deletar/<int:pk>/', deletar_reserva, name='deletar_reserva'),
]
