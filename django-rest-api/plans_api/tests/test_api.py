import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db()


def test_get_plans(client, new_plan):
    response = client.get(reverse('plans_api:plan', kwargs={'pk': new_plan.pk}))
    assert response.status_code == 200
    assert response.json() == {'id': new_plan.pk, 'nome': 'brasilprev', 'susep': '74.648.427/0001-37', 'expiracaoDeVenda': '2025-01-15', 'valorMinimoAporteInicial': '1000.00', \
                                 'valorMinimoAporteExtra': '300.00', 'idadeDeEntrada': 18, 'idadeDeSaida': 70, 'carenciaInicialDeResgate': 5000, 'carenciaEntreResgates': 800}


def test_update_plans(client, new_plan):
    response = client.put(reverse('plans_api:plan', kwargs={'pk': new_plan.pk}),
                          data={'nome': 'brasilprev', 'susep': '74.648.427/0001-37', 'expiracaoDeVenda': '2027-01-15', 'valorMinimoAporteInicial': '500.00', \
                                'valorMinimoAporteExtra': '200.00', 'idadeDeEntrada': 25, 'idadeDeSaida': 60, 'carenciaInicialDeResgate': 3000, 'carenciaEntreResgates': 600},
                          content_type='application/json;')
    assert response.status_code == 200
    assert response.json() == {'id': new_plan.pk}

    response = client.get(reverse('plans_api:plan', kwargs={'pk': new_plan.pk}))
    assert response.status_code == 200
    assert response.json() == {'id': new_plan.pk, 'nome': 'brasilprev', 'susep': '74.648.427/0001-37', 'expiracaoDeVenda': '2027-01-15', 'valorMinimoAporteInicial': '500.00', \
                                'valorMinimoAporteExtra': '200.00', 'idadeDeEntrada': 25, 'idadeDeSaida': 60, 'carenciaInicialDeResgate': 3000, 'carenciaEntreResgates': 600}


def test_create_plans(client):
    response1 = client.post(reverse('plans_api:plans'),
                            data={'nome': 'brasilprev', 'susep': '74.648.427/0001-37', 'expiracaoDeVenda': '2025-01-15', 'valorMinimoAporteInicial': '1000.00', \
                                    'valorMinimoAporteExtra': '300.00', 'idadeDeEntrada': 18, 'idadeDeSaida': 70, 'carenciaInicialDeResgate': 5000, 'carenciaEntreResgates': 800},
                            content_type='application/json;')
    assert response1.status_code == 201

    response = client.get(reverse('plans_api:plan', kwargs={'pk': response1.json()['id']}))
    assert response.status_code == 200
    assert response.json() == {'id': response1.json()['id'], 'nome': 'brasilprev', 'susep': '74.648.427/0001-37', 'expiracaoDeVenda': '2025-01-15', 'valorMinimoAporteInicial': '1000.00', \
                                 'valorMinimoAporteExtra': '300.00', 'idadeDeEntrada': 18, 'idadeDeSaida': 70, 'carenciaInicialDeResgate': 5000, 'carenciaEntreResgates': 800}


def test_delete_plans(client, new_plan):
    response = client.delete(reverse('plans_api:plan', kwargs={'pk': new_plan.pk}))
    assert response.status_code == 204

    response = client.get(reverse('plans_api:plan', kwargs={'pk': new_plan.pk}))
    assert response.status_code == 404