from typing import Dict, Any

Estoque = Dict[str, Dict[str, Any]]

def exibir_menu() -> str:
    return (
        "Adicionar produto\n"
        "Listar produtos\n"
        "Remover produto\n"
        "Atualizar quantidade de produto\n"
        "Sair"
    )


def adicionar_produto(estoque: Estoque, nome: str, quantidade: int, preco: float) -> str:
    if nome in estoque:
        return "Produto já existe no estoque."
    estoque[nome] = {"quantidade": int(quantidade), "preço": float(preco)}
    return f"Produto '{nome}' adicionado com sucesso!"


def listar_produtos(estoque: Estoque) -> str:
    if not estoque:
        return "Estoque vazio."
    linhas = []
    for nome, dados in sorted(estoque.items(), key=lambda item: item[0]):
        linhas.append(f"{nome}: {dados['quantidade']} disponível - R$ {dados['preço']:.2f}")
    return "\n".join(linhas)


def remover_produto(estoque: Estoque, nome: str) -> str:
    if nome not in estoque:
        return "Produto não encontrado."
    del estoque[nome]
    return f"Produto '{nome}' removido com sucesso!"


def atualizar_quantidade(estoque: Estoque, nome: str, nova_quantidade: int) -> str:
    if nome not in estoque:
        return "Produto não encontrado."
    estoque[nome]["quantidade"] = int(nova_quantidade)
    return f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}."

def rodar_programa() -> None:
    estoque: Estoque = {}
    while True:
        print("\n--- Menu Estoque ---")
        print(exibir_menu())
        print("--------------------")
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            nome = input("Nome do produto: ").strip()
            quantidade = int(input("Quantidade: ").strip())
            preco = float(input("Preço: ").strip())
            print(adicionar_produto(estoque, nome, quantidade, preco))

        elif opcao == "2":
            print(listar_produtos(estoque))

        elif opcao == "3":
            nome = input("Nome do produto a remover: ").strip()
            print(remover_produto(estoque, nome))

        elif opcao == "4":
            nome = input("Nome do produto: ").strip()
            nova_qtd = int(input("Nova quantidade: ").strip())
            print(atualizar_quantidade(estoque, nome, nova_qtd))

        elif opcao == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    pass