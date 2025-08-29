class Animal:
    def falar(self):
        pass
class Dog(Animal):
    def falar(self):
        return "Auuuuuuuuu"
class Cat(Animal):
    def falar(self):
        return "Miaaaau te matar!"
animais = [Dog(), Cat()]
for animal in animais:
    print(animal.falar())