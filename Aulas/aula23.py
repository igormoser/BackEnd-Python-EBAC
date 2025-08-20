receber_lista = [input("Digite sua lista de compras: ")]
print(receber_lista)
for i in range(1, 2):
    compras = input()
    receber_lista.append(compras)
receber_lista.sort()

print(receber_lista)
