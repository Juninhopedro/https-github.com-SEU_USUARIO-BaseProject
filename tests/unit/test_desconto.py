import pytest

from src.desconto import calcular_desconto, calcular_frete


def test_aplica_10_por_cento_acima_de_100():
    # Arrange
    valor = 200.0

    # Act
    resultado = calcular_desconto(valor)

    # Assert
    assert resultado == 181.0


@pytest.mark.parametrize(
    ("valor", "esperado"),
    [
        (0.0, 0.0),
        (99.99, 99.99),
        (100.0, 90.0),
        (200.0, 180.0),
    ],
)
def test_calcular_desconto_nos_limites(valor, esperado):
    assert calcular_desconto(valor) == esperado


def test_calcular_desconto_rejeita_valor_negativo():
    with pytest.raises(ValueError, match="Valor não pode ser negativo"):
        calcular_desconto(-0.01)


@pytest.mark.parametrize(
    ("valor_pedido", "distancia_km", "esperado"),
    [
        (200.0, 10.0, 0.0),
        (250.0, 0.0, 0.0),
        (199.99, 0.0, 10.0),
        (100.0, 2.0, 13.0),
    ],
)
def test_calcular_frete(valor_pedido, distancia_km, esperado):
    assert calcular_frete(valor_pedido, distancia_km) == esperado


@pytest.mark.parametrize(
    ("valor_pedido", "distancia_km", "mensagem"),
    [
        (-0.01, 1.0, "Valor do pedido não pode ser negativo"),
        (100.0, -0.01, "Distância não pode ser negativa"),
    ],
)
def test_calcular_frete_rejeita_valores_negativos(
    valor_pedido, distancia_km, mensagem
):
    with pytest.raises(ValueError, match=mensagem):
        calcular_frete(valor_pedido, distancia_km)
