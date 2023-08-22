from django.db import models

class Contract(models.Model):
    idCliente = models.ForeignKey('client_api.Client', on_delete=models.CASCADE)
    idProduto = models.ForeignKey('plans_api.Plans', on_delete=models.CASCADE)
    aporte = models.DecimalField(max_digits=10, decimal_places=2)
    dataDaContratacao = models.DateField()
    cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.idCliente.nome +'-'+ str(self.id)

class Deposit(models.Model):
    idCliente = models.ForeignKey('client_api.Client', on_delete=models.CASCADE)
    idPlano = models.ForeignKey('Contract', on_delete=models.CASCADE)
    valorAporte = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

class Withdraw(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    idPlano = models.ForeignKey('Contract', on_delete=models.CASCADE)
    valorResgate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)