"""
Sistema de Gerenciamento de Estoque
Autor: Igor
Descrição:
    Programa para gerenciar um estoque de produtos usando um dicionário."""

estoque = {}

def adicionar_produto():
    nome = input('Digite o nome do produto: ').strip()
    if nome in estoque:
        print("Produto já existe no estoque!")
        return
    try:
        quantidade = int(input('Quantidade do produto: '))
        preco = float(input("Valor do produto: R$"))
        estoque[nome] = {'quantidade': quantidade, 'preco': preco}
        print(f"Produto {nome} adicionado com sucesso!")
    except ValueError:
        print("Erro: Quantidade e preço devem conter números!!!")

def listar_produtos():
    if not estoque:
        print("Nenhum item no estoque!")
        return
    print("Produtos do estoque:")
    for nome, dados in sorted(estoque.items(), key=lambda x: x[0]):
        print(f"{nome}: {dados["quantidade"]} disponível - R$ {dados['preco']}")

def remover_produto():
    nome = input('Digite o nome do produto: ').strip()
    if nome in estoque:
        del estoque[nome]
        print("Produto removido!")
    else:
        print("Nenhum item no encontrado!")

def atualizar_quantidade():
    nome = input('Digite o nome do produto: ').strip()
    if nome in estoque:
        try:
            nova_quantidade = int(input('Quantidade nova do produto: '))
            estoque[nome]['quantidade'] = nova_quantidade
            print(f"Produto {nome} atualizado com sucesso!")
        except ValueError:
            print("ERRO!!!: A quantidade deve ser utilizando números!")
    else:
        print("Nenhum item no encontrado!")

def menu():
    while True:
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Remover produto")
        print("4 - Atualizar quantidade")
        print("5 - Sair")

        opcao = input("Escolha uma opção!: ")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            remover_produto()
        elif opcao == "4":
            atualizar_quantidade()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
if __name__ == "__main__":
    menu()