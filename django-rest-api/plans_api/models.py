from django.db import models
from localflavor.br.models import BRCNPJField


class Plans(models.Model):
    nome = models.CharField(max_length=50)
    susep = BRCNPJField(unique=True)
    expiracaoDeVenda = models.DateField()
    valorMinimoAporteInicial = models.DecimalField(max_digits=10, decimal_places=2)
    valorMinimoAporteExtra = models.DecimalField(max_digits=10, decimal_places=2)
    idadeDeEntrada = models.IntegerField()
    idadeDeSaida = models.IntegerField()
    carenciaInicialDeResgate = models.IntegerField()
    carenciaEntreResgates = models.IntegerField()

    def __str__(self):
        return self.nome