#Nome: Pedro Vinicius Ernesto Barbosa
#Curso: P2 Informática
#Prof.: Allan Kelvin
list_tarefas = {}

def adcionar_tarefa(list_tarefas):
    while True:
        descrição = input("Digite a descrição da tarefa: ")
        prioridade = input("Digite a prioridade da tarefa (alta, média, baixa): ").lower()
        
        if prioridade in ['alta', 'média', 'baixa']:
            list_tarefas[descrição] = {'Prioridade': prioridade}
            break
        else:
            print("Prioridade inválida! Tente novamente.")
            
def exibir_tarefa(list_tarefas):
    print(list_tarefas)
def concluir_tarefa(list_tarefas):
    exibir_tarefa(list_tarefas)
    while True:
        numdel = int(input("Digite o número da tarefa que deseja concluir: ")) - 1
        if 0 <= numdel < len(list_tarefas):
            tarefa_a_remover = list(list_tarefas.keys())[numdel]
            del list_tarefas[tarefa_a_remover]
            print("Tarefa concluída e removida da lista!")
            return list_tarefas
        else: 
            print("Erro, número inválido. Tente novamente.")

def main():
    print("Escolha uma opção: 1-Adicionar tarefa 2-Exibir tarefas 3-Concluir tarefa 4-Sair")
    while True:
        option = int(input("Opção: "))
        if option == 1:
            adcionar_tarefa(list_tarefas)
        elif option == 2:
            exibir_tarefa(list_tarefas)
        elif option == 3:
            concluir_tarefa(list_tarefas)
        elif option == 4:
            break
        else:
            print("Erro! Tente novamente.")

main()
