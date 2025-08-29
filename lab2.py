tarefas = {}

def adicionar_tarefa(nome):
    if nome in tarefas:
        return "Erro: Tarefa já existente."
    else:
        tarefas[nome] = False
        return f"Tarefa '{nome}' adicionada com sucesso!!"

def listar_tarefas(_):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    else:
        resultado = ["Lista de tarefas:"]
        for nome, concluida in sorted(tarefas.items()):
            status = "✅ Concluída" if concluida else "❌ Não concluída"
            resultado.append(f"{nome}: {status}")
        return "\n".join(resultado)

def remover_tarefa(nome):
    if nome in tarefas:
        del tarefas[nome]
        return f"Tarefa '{nome}' removida com sucesso!"
    else:
        return "Erro: Tarefa não encontrada."

def marcar_concluida(nome):
    if nome in tarefas:
        tarefas[nome] = True
        return f"Tarefa '{nome}' marcada como concluída!"
    else:
        return "Erro: Tarefa não encontrada."

def exibir_menu():
    return (
        "\n1 - Adicionar tarefa"
        "\n2 - Listar tarefas"
        "\n3 - Remover tarefa"
        "\n4 - Marcar tarefa como concluída"
        "\n5 - Sair"
    )

def main():
    while True:
        print(exibir_menu())
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome da tarefa que deseja adicionar: ")
            print(adicionar_tarefa(nome))
        elif opcao == "2":
            print(listar_tarefas(None))
        elif opcao == "3":
            nome = input("Digite o nome da tarefa que deseja remover: ")
            print(remover_tarefa(nome))
        elif opcao == "4":
            nome = input("Digite o nome da tarefa que deseja concluir: ")
            print(marcar_concluida(nome))
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()