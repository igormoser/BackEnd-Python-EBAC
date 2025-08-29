meu_array = [22, 445, 78, 2001, 248, 554, 33]
meu_dicionario = {}
for i in meu_array:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1
somachave = 0
for chave, valor in meu_dicionario.items():
    if valor == 1:
        somachave += chave
print(somachave)
