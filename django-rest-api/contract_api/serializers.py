from datetime import datetime
from rest_framework import serializers 
from .models import Contract, Deposit, Withdraw
from django.db.models import Sum
from . import utils

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = '__all__'


class ContractPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'idCliente', 'idProduto', 'aporte', 'dataDaContratacao')#'__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'idCliente': {'write_only': True},
            'idProduto': {'write_only': True},
            'aporte': {'write_only': True},
            'dataDaContratacao': {'write_only': True},
            'cancelled': {'write_only': True},
        }

    def validate(self, data):
        " Validating client age "
        client_age = utils.age(data['idCliente'].dataDeNascimento)
        if client_age < data['idProduto'].idadeDeEntrada:
            raise serializers.ValidationError({'client_age': 'Idade mínima de entrada neste plano: ' + str(data['idProduto'].idadeDeEntrada)})
        if client_age >= data['idProduto'].idadeDeSaida:
            raise serializers.ValidationError({'client_age': 'Idade máxima de entrada neste plano: ' + str(data['idProduto'].idadeDeSaida)})
        
        " Validating minimun funding entry "
        if data['aporte'] < data['idProduto'].valorMinimoAporteInicial:
            raise serializers.ValidationError({'aporte': 'Valor mínimo para este plano: ' + str(data['idProduto'].valorMinimoAporteInicial)})

        " Validating contract expiration date "
        if data['dataDaContratacao'] > data['idProduto'].expiracaoDeVenda:
            raise serializers.ValidationError({'dataDaContratacao': 'O plano escolhido está vencido: ' + str(data['idProduto'].expiracaoDeVenda)})
        return data


class DepositPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'idCliente': {'write_only': True},
            'idPlano': {'write_only': True},
            'valorAporte': {'write_only': True},
        }

    def validate(self, data):
        " Validating extra funding "
        if data['idPlano'].cancelled:
            raise serializers.ValidationError({'cancelled': 'Este contrato já foi cancelado devido a saldo insuficiente.'})

        if data['valorAporte'] < data['idPlano'].idProduto.valorMinimoAporteExtra:
            raise serializers.ValidationError({'aporte': 'Valor mínimo de aporte extra para este plano: ' + str(data['idPlano'].idProduto.valorMinimoAporteExtra)})

        return data

class WithdrawPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('id', 'idPlano', 'valorResgate')
        extra_kwargs = {
            'id': {'read_only': True},
            'idPlano': {'write_only': True},
            'valorResgate': {'write_only': True},
        }

    def validate(self, data):
        " Validating if contract is not cancelled "
        if data['idPlano'].cancelled:
            raise serializers.ValidationError({'cancelled': 'Este contrato já foi cancelado devido a saldo insuficiente.'})


        " Validating minimum period from contract "
        today = datetime.now().date()
        days_from_contract = (today - data['idPlano'].dataDaContratacao).days
        if days_from_contract < data['idPlano'].idProduto.carenciaInicialDeResgate:
            raise serializers.ValidationError({'carencia': 'Carência mínima de dias não atingida: ' + str(days_from_contract) + \
                                                                        '. Necessário: ' + str(data['idPlano'].idProduto.carenciaInicialDeResgate) })

        " Validating minimum period from last withdraw "
        previous_withdraw = Withdraw.objects.filter(idPlano=data['idPlano']).order_by('-created_at')
        previous_withdraw_date = previous_withdraw.first().created_at.date()
        days_from_last_withdraw = (today - previous_withdraw_date).days

        if days_from_last_withdraw < data['idPlano'].idProduto.carenciaEntreResgates:
            raise serializers.ValidationError({'carência': 'Tempo mínimo entre resgates para este plano: ' + str(days_from_last_withdraw) + \
                                                                        '. Necessário: ' + str(data['idPlano'].idProduto.carenciaEntreResgates)})

        " Validating available funds to withdraw "
        contract = Contract.objects.get(id=data['idPlano'].id)
        initial_deposit = contract.aporte
        total_deposits = Deposit.objects.filter(idPlano=data['idPlano']).aggregate(Sum('valorAporte'))['valorAporte__sum']
        total_withdraws = previous_withdraw.aggregate(Sum('valorResgate'))['valorResgate__sum']

        contract_total = initial_deposit + total_deposits - total_withdraws
        if contract_total < data['valorResgate']:
            raise serializers.ValidationError({'valorResgate': 'Valor solicitado não disponível. Total disponível: ' + str(contract_total)})

        " Cancelling contract if there are no funds available "
        if contract_total - data['valorResgate'] == 0:
            # another way without cancelled field is checking if the sum of all deposits and withdraws are equal to 0
            contract.cancelled = True
            contract.save()
        return data