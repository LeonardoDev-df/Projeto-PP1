from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum  # Importe o Sum do Django models
from .models import Reserva
from .forms import ReservaForm
from datetime import datetime, time
from django.contrib import messages


def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "listar_reservas.html", {"reservas": reservas})



def criar_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)

            # Verificar regras de negócio
            if reserva.horario < time(11, 0):
                messages.add_message(request, messages.ERROR, "Desculpe, não é possível fazer reservas antes das 11h.")
                return render(
                    request,
                    "booking/criar_reserva.html",
                    {"form": form, "messages": messages.get_messages(request)},
                )

            reservas_no_horario = Reserva.objects.filter(
                data=reserva.data, horario=reserva.horario
            ).count()
            mesas_reservadas = Reserva.objects.filter(
                status='confirmada'
            ).aggregate(total_mesas_reservadas=Sum('mesas_reservadas'))['total_mesas_reservadas'] or 0
            
            mesas_disponiveis = 5
            mesas_disponiveis = mesas_disponiveis - mesas_reservadas
            
            if mesas_disponiveis < reserva.mesas_reservadas:
                #mensagem = 'Desculpe, o restaurante está lotado. Não é possível fazer mais reservas de mesa.'
                messages.add_message(request, messages.ERROR, 'Desculpe, o restaurante está lotado. Não é possível fazer mais reservas de mesa.')
                return render(
                    request,
                    "booking/criar_reserva.html",
                    {"form": form, "messages": messages.get_messages(request)},
                )

            reserva.save()
            return redirect("listar_reservas")
    else:
        form = ReservaForm()

    return render(request, "booking/criar_reserva.html", {"form": form, "messages": messages.get_messages(request)})


def confirmar_chegada(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    reserva.confirmar_chegada()
    reserva.atualizar_status_mesas()
    return redirect("listar_reservas")


def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    reserva.cancelar_reserva()
    reserva.atualizar_status_mesas()
    return redirect("listar_reservas")


def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            reserva = form.save(commit=False)
            # Verificar regras de negócio
            if reserva.horario < time(11, 0):
                mensagem = "Desculpe, não é possível fazer reservas antes das 11h."
                return render(
                    request,
                    "booking/criar_reserva.html",
                    {"form": form, "mensagem": mensagem},
                )

            reservas_no_horario = Reserva.objects.filter(
                data=reserva.data, horario=reserva.horario
            ).count()
            mesas_reservadas = Reserva.objects.filter(
                status='confirmada'
            ).aggregate(total_mesas_reservadas=Sum('mesas_reservadas'))['total_mesas_reservadas'] or 0
            
            mesas_disponiveis = 5 - mesas_reservadas
            
            if mesas_disponiveis < reserva.mesas_reservadas:
                mensagem = (
                    'Desculpe, o restaurante está lotado. Não é possível fazer mais reservas de mesa.'
                )
                return render(
                    request,
                    "booking/criar_reserva.html",
                    {"form": form, "mensagem": mensagem},
                )

            reserva.save()
            return redirect("listar_reservas")
    else:
        form = ReservaForm(instance=reserva)

    return render(
        request, "booking/editar_reserva.html", {"form": form, "reserva": reserva}
    )


def deletar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        reserva.delete()
        return redirect("listar_reservas")
    return render(request, "booking/deletar_reserva.html", {"reserva": reserva})
