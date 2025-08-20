while True:

    try:
        numero = int(input('digite um numero: '))
        resultado = 10 / numero
        print(resultado)
    except ValueError:
        print('digite um NÚMERO inteiro!Sua MULA')
    except ZeroDivisionError:
        print('ERRO!Não se pode dividir por 0')
        break