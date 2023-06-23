from django.db import models

class Reserva(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    )

    def confirmar_chegada(self):
        if not self.chegada_confirmada:
            self.chegada_confirmada = True
            self.status = 'confirmada'  # Atualiza o status para 'confirmada'
            self.save()

    def cancelar_reserva(self):
        if not self.chegada_confirmada:
            self.status = 'cancelada'
            self.save()

    def atualizar_status_mesas(self):
        if self.status == 'confirmada':
            self.mesas_reservadas = 1
        else:
            self.mesas_reservadas = -1
        self.save()

     # Campos do modelo
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    numero_pessoas = models.PositiveIntegerField()
    data = models.DateField()
    horario = models.TimeField()
    mesas_reservadas = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    chegada_confirmada = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Reserva para {self.nome} em {self.data} às {self.horario}'

    objects = models.Manager()