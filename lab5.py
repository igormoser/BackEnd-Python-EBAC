# ==============================
# Funções básicas
# ==============================

def obter_dados_livro(titulo: str, autor: str, quantidade: int) -> dict:
    """
    Retorna um dicionário com os dados de um livro.
    """
    return {"titulo": titulo.strip(), "autor": autor.strip(), "quantidade": quantidade}


def obter_quantidade_livro(quantidade: int) -> int | None:
    """
    Valida se a quantidade é um inteiro >= 0.
    Retorna a quantidade se válido, senão None.
    """
    try:
        q = int(quantidade)
        return q if q >= 0 else None
    except (ValueError, TypeError):
        return None


def validar_livro_existe(biblioteca: dict, titulo: str) -> bool:
    """
    Retorna True se o livro existir na biblioteca, False caso contrário.
    """
    return titulo in biblioteca


def obter_quantidade_livro_para_emprestimo(biblioteca: dict, titulo: str, quantidade: int) -> bool:
    """
    Valida se é possível emprestar a quantidade solicitada do livro.
    """
    if not validar_livro_existe(biblioteca, titulo):
        return False
    if quantidade <= 0:
        return False
    if quantidade > biblioteca[titulo]["quantidade"]:
        return False
    return True


# ==============================
# Operações da biblioteca
# ==============================

def adicionar_livro(biblioteca: dict, titulo: str, autor: str, quantidade: int) -> str:
    """
    Adiciona um livro ao acervo, caso não exista.
    """
    if validar_livro_existe(biblioteca, titulo):
        return "Livro já cadastrado."
    q = obter_quantidade_livro(quantidade)
    if q is None:
        return "Quantidade inválida."
    biblioteca[titulo] = {"autor": autor, "quantidade": q}
    return f"Livro '{titulo}' adicionado com sucesso!"


def listar_livros(biblioteca: dict) -> str:
    """
    Retorna os livros em ordem alfabética no formato:
    título - autor - quantidade disponível
    """
    if not biblioteca:
        return "Nenhum livro cadastrado."
    linhas = []
    for titulo in sorted(biblioteca.keys()):
        dados = biblioteca[titulo]
        linhas.append(f"{titulo} - {dados['autor']} - {dados['quantidade']} disponível(is)")
    return "\n".join(linhas)


def remover_livro(biblioteca: dict, titulo: str) -> str:
    """
    Remove um livro se existir.
    """
    if not validar_livro_existe(biblioteca, titulo):
        return "Livro não encontrado."
    del biblioteca[titulo]
    return f"Livro '{titulo}' removido com sucesso!"


def atualizar_quantidade(biblioteca: dict, titulo: str, nova_quantidade: int) -> str:
    """
    Atualiza a quantidade de exemplares de um livro.
    """
    if not validar_livro_existe(biblioteca, titulo):
        return "Livro não encontrado."
    q = obter_quantidade_livro(nova_quantidade)
    if q is None:
        return "Quantidade inválida."
    biblioteca[titulo]["quantidade"] = q
    return "Quantidade atualizada com sucesso!"


# ==============================
# Empréstimos
# ==============================

def registrar_emprestimo(biblioteca: dict, historico: list, titulo: str, quantidade: int) -> str:
    """
    Registra um empréstimo se houver exemplares suficientes.
    """
    if not obter_quantidade_livro_para_emprestimo(biblioteca, titulo, quantidade):
        return "Não foi possível realizar o empréstimo."
    biblioteca[titulo]["quantidade"] -= quantidade
    historico.append({"titulo": titulo, "quantidade": quantidade})
    return f"Empréstimo de {quantidade} exemplar(es) do livro '{titulo}' registrado!"


def exibir_historico_emprestimos(historico: list) -> str:
    """
    Retorna o histórico de empréstimos em formato de string.
    """
    if not historico:
        return "Nenhum empréstimo registrado."
    return "\n".join(f"{item['titulo']} - {item['quantidade']} exemplar(es)" for item in historico)


# ==============================
# Menu interativo
# ==============================

def exibir_menu() -> str:
    """
    Retorna o texto do menu.
    """
    return (
        "1 - Adicionar livro\n"
        "2 - Listar livros\n"
        "3 - Remover livro\n"
        "4 - Atualizar quantidade de livros\n"
        "5 - Registrar empréstimo\n"
        "6 - Exibir histórico de empréstimos\n"
        "7 - Sair"
    )


def menu():
    """
    Fluxo principal do programa.
    """
    biblioteca = {}
    historico = []

    while True:
        print("\n=== Sistema de Gerenciamento de Biblioteca ===")
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            quantidade = int(input("Quantidade: "))
            print(adicionar_livro(biblioteca, titulo, autor, quantidade))

        elif opcao == "2":
            print(listar_livros(biblioteca))

        elif opcao == "3":
            titulo = input("Título: ")
            print(remover_livro(biblioteca, titulo))

        elif opcao == "4":
            titulo = input("Título: ")
            quantidade = int(input("Nova quantidade: "))
            print(atualizar_quantidade(biblioteca, titulo, quantidade))

        elif opcao == "5":
            titulo = input("Título: ")
            quantidade = int(input("Quantidade a emprestar: "))
            print(registrar_emprestimo(biblioteca, historico, titulo, quantidade))

        elif opcao == "6":
            print(exibir_historico_emprestimos(historico))

        elif opcao == "7":
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida, tente novamente.")


# ==============================
# Bloco principal
# ==============================

if __name__ == "__main__":
    menu()
