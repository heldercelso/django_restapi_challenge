import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db()


def test_get_contract(client, new_contract):
    response = client.get(reverse('contract_api:contract', kwargs={'pk': new_contract.pk}))
    assert response.status_code == 200
    assert response.json() == {'id': new_contract.pk, 'aporte': '6000.00', 'dataDaContratacao': '2023-01-15', 'cancelled': False, 'idCliente': new_contract.idCliente.pk, 'idProduto': new_contract.idProduto.pk}


def test_update_contract(client, new_contract):
    response = client.put(reverse('contract_api:contract', kwargs={'pk': new_contract.pk}),
                          data={'aporte': '5000.00', 'dataDaContratacao': '2023-01-16', 'cancelled': False, 'idCliente': new_contract.idCliente.pk, 'idProduto': new_contract.idProduto.pk},
                          content_type='application/json;')
    assert response.status_code == 200
    assert response.json() == {'id': new_contract.pk}

    response = client.get(reverse('contract_api:contract', kwargs={'pk': new_contract.pk}))
    assert response.status_code == 200
    assert response.json() == {'id': new_contract.pk, 'aporte': '5000.00', 'dataDaContratacao': '2023-01-16', 'cancelled': False, 'idCliente': new_contract.idCliente.pk, 'idProduto': new_contract.idProduto.pk}


def test_create_contract(client, new_user, new_plan):
    response = client.post(reverse('contract_api:contracts'),
                            data={'aporte': '6000.00', 'dataDaContratacao': '2023-01-15', 'cancelled': False, 'idCliente': new_user.pk, 'idProduto': new_plan.pk},
                            content_type='application/json;')
    assert response.json() == {'id': 3}
    assert response.status_code == 201
    assert response.json() == {'id': 3}

    response = client.get(reverse('contract_api:contracts'))
    assert response.status_code == 200
    assert response.json() == [{'id': 3, 'aporte': '6000.00', 'dataDaContratacao': '2023-01-15', 'cancelled': False, 'idCliente': new_user.pk, 'idProduto': new_plan.pk}]


def test_delete_contract(client, new_contract):
    response = client.delete(reverse('contract_api:contract', kwargs={'pk': '4'}))
    assert response.status_code == 204

    response = client.get(reverse('contract_api:contract', kwargs={'pk': '4'}))
    assert response.status_code == 404