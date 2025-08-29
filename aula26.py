novo_array = ["12", "325", "12", "325", "2154684231", "11"]
contador = 0
for i in novo_array:
    if len(i) % 2 == 0:
        contador += 1
print(contador)