from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('nome', 'email', 'numero_pessoas', 'data', 'horario', 'mesas_reservadas')
