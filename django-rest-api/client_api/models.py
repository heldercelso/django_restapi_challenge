from django.db import models
from localflavor.br.models import BRCPFField

class Client(models.Model):
    GENDER_CHOICES = (
        ('H', 'Homem'),
        ('M', 'Mulher'),
    )
    cpf = BRCPFField(unique=True)
    nome = models.TextField()
    email = models.EmailField()
    dataDeNascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES)
    rendaMensal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome