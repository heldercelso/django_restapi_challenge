import pytest
from client_api.models import Client
from plans_api.models import Plans
from contract_api.models import Contract

@pytest.fixture
def new_user():
    data = {
                'cpf': '553.396.320-08',
                'nome': 'Fulano',
                'email': 'fulano@example.com',
                'dataDeNascimento': '2000-01-15',
                'sexo': 'H',
                'rendaMensal': '3000.00'
            }
    user = Client.objects.get_or_create(cpf=data['cpf'], nome=data['nome'], email=data['email'], dataDeNascimento=data['dataDeNascimento'], sexo=data['sexo'], rendaMensal=data['rendaMensal'])[0]
    user.save()

    return user

@pytest.fixture
def new_plan():
    data = {
                'nome': 'brasilprev',
                'susep': '74.648.427/0001-37',
                'expiracaoDeVenda': '2025-01-15',
                'valorMinimoAporteInicial': '1000',
                'valorMinimoAporteExtra': '300',
                'idadeDeEntrada': 18,
                'idadeDeSaida': 70,
                'carenciaInicialDeResgate': 5000,
                'carenciaEntreResgates': 800
            }
    plan = Plans.objects.get_or_create(nome=data['nome'], susep=data['susep'], expiracaoDeVenda=data['expiracaoDeVenda'], valorMinimoAporteInicial=data['valorMinimoAporteInicial'], valorMinimoAporteExtra=data['valorMinimoAporteExtra'],
                                        idadeDeEntrada=data['idadeDeEntrada'], idadeDeSaida=data['idadeDeSaida'], carenciaInicialDeResgate=data['carenciaInicialDeResgate'], carenciaEntreResgates=data['carenciaEntreResgates'])[0]
    plan.save()

    return plan

@pytest.fixture
def new_contract(new_user, new_plan):
    data = {
                'aporte': '6000',
                'dataDaContratacao': '2023-01-15',
                'idCliente': new_user,
                'idProduto': new_plan
            }
    contract = Contract.objects.get_or_create(aporte=data['aporte'], dataDaContratacao=data['dataDaContratacao'], idCliente=data['idCliente'], idProduto=data['idProduto'])[0]
    contract.save()

    return contract