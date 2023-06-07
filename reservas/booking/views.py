from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'booking/listar_reservas.html', {'reservas': reservas})

def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'booking/criar_reserva.html', {'form': form})

def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'booking/editar_reserva.html', {'form': form})

def deletar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('listar_reservas')
    return render(request, 'booking/deletar_reserva.html', {'reserva': reserva})
