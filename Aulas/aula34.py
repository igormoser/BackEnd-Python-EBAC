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