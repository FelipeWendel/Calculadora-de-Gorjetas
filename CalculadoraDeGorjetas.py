def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta com base no valor total da conta e na porcentagem da gorjeta desejada.

    Args:
        valor_conta (float): Valor total da conta.
        porcentagem_gorjeta (float): Porcentagem da gorjeta desejada.

    Returns:
        float: Valor da gorjeta.
    """
    gorjeta = (valor_conta / 100) * porcentagem_gorjeta
    return gorjeta

def main():
    valor_conta = float(input("Digite o valor total da conta: "))
    porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta desejada: "))

    gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

    print(f"Valor da gorjeta: R${gorjeta:.2f}")
    print(f"Valor total com gorjeta: R${valor_conta + gorjeta:.2f}")

if __name__ == "__main__":
    main()