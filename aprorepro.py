print("Vamos saber se você está, aprovado, em recuperação ou reprovado!")
nota = float(input("Digite sua nota: "))
if nota >= 7.0:
    print("Parabéns você foi aprovado!")
elif nota >= 5.0 and nota <= 7.0:
    print("Você está de recuperação!")
else:
    print("Você está reprovado!")