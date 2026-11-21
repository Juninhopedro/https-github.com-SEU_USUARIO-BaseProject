
import pytest
from fastapi.testclient import TestClient

from src.app import PEDIDOS_DB, app

client = TestClient(app)


@pytest.fixture(autouse=True)
def limpar_pedidos():
    PEDIDOS_DB.clear()
    yield
    PEDIDOS_DB.clear()


def test_health_check_retorna_200():
    resp = client.get("/health")

    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_criar_pedido_com_desconto_e_frete():
    resp = client.post(
        "/pedidos",
        json={"item": "Livro", "valor": 120.0, "distancia_km": 5.0},
    )

    assert resp.status_code == 201
    assert resp.json()["total_com_desconto"] == 108.0
    assert resp.json()["frete"] == 17.5
    assert resp.json()["total_final"] == 125.5


def test_criar_pedido_com_valor_negativo_retorna_400():
    resp = client.post(
        "/pedidos",
        json={"item": "Livro", "valor": -1.0, "distancia_km": 5.0},
    )

    assert resp.status_code == 400
    assert resp.json()["detail"] == "Valor não pode ser negativo"


def test_criar_pedido_com_item_vazio_retorna_400():
    resp = client.post(
        "/pedidos",
        json={"item": "  ", "valor": 50.0, "distancia_km": 1.0},
    )

    assert resp.status_code == 400
    assert resp.json()["detail"] == "Nome do item é obrigatório"


def test_listar_pedidos_inclui_pedido_criado():
    criado = client.post(
        "/pedidos",
        json={"item": "Caderno", "valor": 50.0, "distancia_km": 2.0},
    )

    assert criado.status_code == 201
    resp = client.get("/pedidos")

    assert resp.status_code == 200
    assert criado.json() in resp.json()
