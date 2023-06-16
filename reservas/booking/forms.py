from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('data', 'nome', 'email', 'numero_pessoas', 'horario')
        
