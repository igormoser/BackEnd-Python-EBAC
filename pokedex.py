"""
Pokédex - Gerenciador de Pokémon
--------------------------------
Instruções de execução:
1. Salve este arquivo como `pokedex.py`.
2. Execute no terminal com: python pokedex.py
3. Não há dependências externas além do Python 3.x.

Funcionalidades:
- Adicionar Pokémon
- Listar Pokémon
- Remover Pokémon
- Atualizar nível de Pokémon
- Registrar captura
- Exibir histórico de capturas
- Sair do programa
"""

# Estrutura de dados principal
pokedex = {}  # Ex: {"Pikachu": {"tipo": "Elétrico", "nível": 25, "capturas": 0}}
historico_capturas = []  # Lista de registros de capturas


# ------------------------- Funções -------------------------

def adicionar_pokemon():
    """Adiciona um Pokémon na Pokédex."""
    nome = input("Nome do Pokémon: ").capitalize()
    tipo = input("Tipo do Pokémon (Ex: Fogo, Água, Elétrico...): ").capitalize()

    try:
        nivel = int(input("Nível do Pokémon (1-100): "))
        if nivel < 1 or nivel > 100:
            print("❌ O nível deve ser entre 1 e 100.")
            return
    except ValueError:
        print("❌ O nível deve ser um número inteiro.")
        return

    if nome in pokedex:
        print(f"❌ O Pokémon {nome} já está cadastrado!")
    else:
        pokedex[nome] = {"tipo": tipo, "nível": nivel, "capturas": 0}
        print(f"✅ Pokémon {nome} adicionado com sucesso!")


def listar_pokemon():
    """Lista todos os Pokémon em ordem alfabética."""
    if not pokedex:
        print("📭 Nenhum Pokémon cadastrado.")
        return

    print("\n📜 Lista de Pokémon:")
    for nome in sorted(pokedex.keys()):
        dados = pokedex[nome]
        print(f"- {nome} | Tipo: {dados['tipo']} | Nível: {dados['nível']} | Capturas: {dados['capturas']}")
    print()


def remover_pokemon():
    """Remove um Pokémon da Pokédex."""
    nome = input("Nome do Pokémon a remover: ").capitalize()
    if nome in pokedex:
        del pokedex[nome]
        print(f"🗑️ Pokémon {nome} removido com sucesso.")
    else:
        print("❌ Pokémon não encontrado.")


def atualizar_nivel():
    """Atualiza o nível de um Pokémon existente."""
    nome = input("Nome do Pokémon: ").capitalize()
    if nome in pokedex:
        try:
            novo_nivel = int(input("Novo nível (1-100): "))
            if 1 <= novo_nivel <= 100:
                pokedex[nome]["nível"] = novo_nivel
                print(f"✅ Nível de {nome} atualizado para {novo_nivel}.")
            else:
                print("❌ O nível deve ser entre 1 e 100.")
        except ValueError:
            print("❌ O nível deve ser um número inteiro.")
    else:
        print("❌ Pokémon não encontrado.")


def registrar_captura():
    """Registra captura de um Pokémon."""
    nome = input("Nome do Pokémon: ").capitalize()
    if nome in pokedex:
        try:
            quantidade = int(input("Quantidade de capturas: "))
            if quantidade > 0:
                pokedex[nome]["capturas"] += quantidade
                historico_capturas.append((nome, quantidade))
                print(f"✅ {quantidade} captura(s) de {nome} registrada(s).")
            else:
                print("❌ A quantidade deve ser maior que 0.")
        except ValueError:
            print("❌ A quantidade deve ser um número inteiro.")
    else:
        print("❌ Pokémon não encontrado.")


def exibir_historico():
    """Exibe o histórico de capturas."""
    if not historico_capturas:
        print("📭 Nenhuma captura registrada.")
        return

    print("\n📖 Histórico de Capturas:")
    for idx, (nome, qtd) in enumerate(historico_capturas, start=1):
        print(f"{idx}. {nome} - {qtd} vez(es)")
    print()


# ------------------------- Menu Principal -------------------------

def menu():
    while True:
        print("\n--- Pokédex ---")
        print("1. Adicionar Pokémon")
        print("2. Listar Pokémon")
        print("3. Remover Pokémon")
        print("4. Atualizar nível de Pokémon")
        print("5. Registrar captura")
        print("6. Exibir histórico de capturas")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_pokemon()
        elif opcao == "2":
            listar_pokemon()
        elif opcao == "3":
            remover_pokemon()
        elif opcao == "4":
            atualizar_nivel()
        elif opcao == "5":
            registrar_captura()
        elif opcao == "6":
            exibir_historico()
        elif opcao == "7":
            print("👋 Encerrando a Pokédex. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


# ------------------------- Execução -------------------------
if __name__ == "__main__":
    menu()
