def counter_function():
    yield 1
    yield 2
    yield 3
contador = counter_function()
print(contador)
print(next(contador))