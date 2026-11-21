from src.desconto import calcular_desconto


def test_aplica_10_por_cento_acima_de_100():
    # Arrange
    valor = 200.0

    # Act
    resultado = calcular_desconto(valor)

    # Assert
    assert resultado == 180.0


# TODO (Prática 1):
# 1. Use @pytest.mark.parametrize para testar valores de borda: 0, 99.99, 100.0, 200.0
# 2. Use pytest.raises(ValueError) para validar valores negativos em calcular_desconto
# 3. Crie testes unitários para calcular_frete (valor >= 200 grátis, < 200 com distância e erros negativos)
# 4. Crie um teste para aprovar_pedido usando MagicMock no parâmetro mailer
