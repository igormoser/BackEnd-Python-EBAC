class Pokemon:
    def __init__(self, nome, hp, tipo, ataque, altura, peso):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso
    def nomepokemon(self):
        print(f"O pokemon se chama: {self.nome}")

    def hp(self):
        print(f"A vida do Pokemon é de: {self.hp}")

    def tipo(self):
        print(f"O Pokemon é do tipo: {self.tipo}")

    def ataque(self):
        print(f"O ataque do Pokemon é: {self.ataque}")

    def altura(self):
        print(f"Altura de : {self.altura}")

    def peso(self):
        print(f"E o peso é: {self.peso}")


charmander = Pokemon("Charmander", 1000, "Fogo", "Foguin", 50, 100)
charmilion = Pokemon("Charmilion", 1500, "Fogo", "Fogão", 70, 150)
charizard = Pokemon("Charizard", 5000, "Fogo", "Super Fogão", 220, 250)