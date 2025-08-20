meu_numero = int(input())
minha_string = str(meu_numero)
if minha_string == minha_string[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")