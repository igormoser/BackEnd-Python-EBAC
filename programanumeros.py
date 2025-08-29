numero1, numero2, numero3 = map(int, input().split())

programa_n = []

programa_n.append(numero1)
programa_n.append(numero2)
programa_n.append(numero3)

programa_n.sort()
print(programa_n[1])