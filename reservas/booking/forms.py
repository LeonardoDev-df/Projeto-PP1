from django import forms
from datetime import date
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('data', 'nome', 'email', 'numero_pessoas', 'horario') 

    def clean_data(self):
        data = self.cleaned_data.get('data')

        if data and data < date.today():
            raise forms.ValidationError('A data da reserva não pode ser anterior à data atual.')

        return data

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['data'] = self.clean_data()
        return cleaned_data
