from django.db import models

class Reserva(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    
    def __str__(self):
        return str(self.nome)

