from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_health_check_retorna_200():
    resp = client.get("/health")

    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


# TODO (Prática 2):
# 1. Testar POST /pedidos com valor >= 100 e distância > 0 (status 201 e total_final calculado)
# 2. Testar POST /pedidos com valor negativo (status 400 e mensagem de erro)
# 3. Testar POST /pedidos com item vazio (status 400)
# 4. Testar GET /pedidos verificando se o pedido criado aparece na lista
