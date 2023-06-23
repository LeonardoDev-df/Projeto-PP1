from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum  # Importe o Sum do Django models
from .models import Reserva
from .forms import ReservaForm
from datetime import date, datetime, time, timedelta
from django.contrib import messages
from django.utils import timezone




def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "listar_reservas.html", {"reservas": reservas})



def criar_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)

            # Verificar regra de negócio: Permitir reservas apenas no dia atual
            data_atual = date.today()
            # Formatar a data no formato dia/mês/ano
            data_formatada = data_atual.strftime('%d/%m/%Y')
            
                 # Verificar regra de negócio: Não reservar com mais de 3 dias de antecedência
            data_limite = data_atual + timedelta(days=3)

            if reserva.data < data_atual or reserva.data > data_limite:
                messages.add_message(request, messages.ERROR, "Desculpe, só é possível fazer reservas com até 3 dias de antecedência.")
                return render(request, "booking/criar_reserva.html", {"form": form, "messages": messages.get_messages(request)})
            

            # Verificar regras de negócio
            horario = request.POST.get('horario')  # Obtém o valor do campo de horário do POST
            horario_obj = datetime.strptime(horario, '%H:%M').time()  # Converte para um objeto time

            if horario_obj < time(11, 0):
                    messages.add_message(request, messages.ERROR, "Desculpe, não é possível fazer reservas antes das 11h.")
                    return render(
                        request,
                        "booking/criar_reserva.html",
                        {"form": form, "messages": messages.get_messages(request)},
                    )

            reservas_no_horario = Reserva.objects.filter(data=reserva.data, horario=reserva.horario).count()
            mesas_reservadas = Reserva.objects.filter(status='confirmada').aggregate(total_mesas_reservadas=Sum('mesas_reservadas'))['total_mesas_reservadas'] or 0

            mesas_disponiveis = 10
            mesas_disponiveis = mesas_disponiveis - mesas_reservadas

            if mesas_disponiveis < reserva.mesas_reservadas:
                messages.add_message(request, messages.ERROR, 'Desculpe, o restaurante está lotado. Não é possível fazer mais reservas de mesa.')
                return render(
                    request,
                    "booking/criar_reserva.html",
                    {"form": form, "messages": messages.get_messages(request)},
                )

            # Mensagem de sucesso
            #messages.add_message(request, messages.SUCCESS, "Reserva criada com sucesso!")

            reserva.save()
            return redirect("listar_reservas")
    else:
         form = ReservaForm(initial={'numero_pessoas': 1})

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
            
            mesas_disponiveis = 10 - mesas_reservadas
            
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
