array = [1,2,3,4,5,7,1,2,3,4,4,4,7]
dicionario = {}
for i in array:
    if i not in dicionario:
        dicionario[i] = 1
    else:
        dicionario[i] += 1
for chave, valor in dicionario.items():
    if chave == valor:
        print(chave)