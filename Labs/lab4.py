def solicitar_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("⚠️ Valor inválido! Digite apenas números inteiros.")


def menu_operacoes():
    operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
    [print(f"{i+1} - {op}") for i, op in enumerate(operacoes)]
    return operacoes


def realizar_operacao():
    num1 = solicitar_numero("Digite o primeiro número: ")
    num2 = solicitar_numero("Digite o segundo número: ")

    print("\nEscolha uma operação:")
    operacoes = menu_operacoes()
    opcao = input("\nSelecione a operação desejada (1-4): ")

    operacoes_lambda = {
        "1": lambda x, y: x + y,
        "2": lambda x, y: x - y,
        "3": lambda x, y: x * y,
        "4": lambda x, y: x / y if y != 0 else None
    }

    if opcao not in operacoes_lambda:
        print("⚠️ Opção inválida! Tente novamente.")
        return

    if opcao == "4" and num2 == 0:
        while num2 == 0:
            print("❌ Divisão por zero não é permitida.")
            num2 = solicitar_numero("Digite outro número para o divisor: ")

    resultado = operacoes_lambda[opcao](num1, num2)
    print(f"\nVocê escolheu: {operacoes[int(opcao) - 1]}")
    print(f"O resultado é: {resultado}\n")


while True:
    realizar_operacao()
    resposta = input("Deseja realizar outra operação? (S/N): ").strip().lower()
    if resposta != 's':
        print("\nObrigado por usar a calculadora. Até a próxima! 👋")
        break
