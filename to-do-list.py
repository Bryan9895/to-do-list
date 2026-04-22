tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)

def listar_tarefas():
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)

while True:
    print("\n1 - Adicionar | 2 - Listar | 3 - Remover | 4 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        indice = int(input("Número da tarefa: ")) - 1
        remover_tarefa(indice)
    elif opcao == "4":
        break