from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_dever_retornar_hello_world():
    """Teste  de tres etapas
    A: Arrange - Arranjo
    A: Act - executa a coisa (o SUT)
    A: Assert - Valida o resultado
    """
    client = TestClient(app)
    response = client.get('/')
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK


def test_noise():
    client = TestClient(app)
    response = client.get('/noise')
    resposta = response.text
    print(dir(response))
    print(response.http_version)

    assert '<h1>Hello World</h1>' in resposta
    assert response.status_code == HTTPStatus.OK
