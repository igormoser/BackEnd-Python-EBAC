print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    print("O resultado é:",num1 + num2)
elif opcao == "2":
    print(num1 - num2)
elif opcao == "3":
    print(num1 * num2)
elif opcao == "4":
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        print(num1 / num2)
print("Obrigado por utilizar o programa.")
continuar = input("Deseja continuar? [S/N]: ")
if continuar == "N":
    print("Obrigado por utilizar o programa.")
if continuar == "S":
    opcao = input("Digite o número da operação desejada: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
if opcao == "1":
    print("O resultado é:",num1 + num2)
elif opcao == "2":
    print(num1 - num2)
elif opcao == "3":
    print(num1 * num2)
elif opcao == "4":
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        print(num1 / num2)
print("Obrigado por utilizar o programa.")

