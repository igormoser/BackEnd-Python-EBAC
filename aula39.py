def meu_decorator(func):
    def wrapper():
        print('executando')
        func()
        print('executado')
    return wrapper
@meu_decorator
def executando():
    print('executando')
def executador():
    print('executador')
executador()
executando()