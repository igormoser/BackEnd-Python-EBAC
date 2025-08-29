print("Olá, vamos calcular?")
print("Se o que deseja é Soma,digite 1.")
print("Se o que deseja é Subtração,digite 2.")
print("Se o que deseja é Multiplicação,digite 3.")
print("Se o que deseja é Divisão,digite 4.")
print("Por favor apenas utilize números inteiros.")

def realizar_operacao():
    pass
opcao = input("Selecione a operação que deseja digitando um número: ")
num1 = int(input("Digite o primeiro número desejado: "))
num2 = int(input("Digite o segundo número desejado: "))
resultado1 = num1 + num2
resultado2 = num1 - num2
resultado3 = num1 * num2
resultado4 = num1 / num2

if opcao == "1":
    print("O resultado da Soma de {} + {} é: {}".format(num1, num2, resultado1))

elif opcao == "2":
    print("O resultado da Subtração de {} - {} é: {}".format(num1, num2, resultado2))

elif  opcao == "3":
    print("O resultado da Multipicação de {} * {} é: {}".format(num1, num2, resultado3))
elif opcao == "4":
    if num2 == 0:
        print(ZeroDivisionError("Erro! Divisão por Zero não é permitida."))
    else:
        print("O resultado da Divisão de {} / {} é: {}".format(num1, num2, resultado4))
while True:
    realizar_operacao()
    resposta = input("Deseja realizar outra operação? (s/n): ").strip().lower()
    if resposta != 's':
        print("Obrigado por usar a calculadora. Até a próxima!")
    else:
        break