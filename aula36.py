class Animal:
    def __init__(self, nome):
        self.nome = nome
    def comer(self):
        print(f"O {self.nome} está comendo!")
class Tiger(Animal):
    def matar(self):
        print(f"{self.nome} Matou você!")
tigrao = Tiger("Tigrao")
tigrao.matar()