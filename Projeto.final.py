def adicionar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    print("\n")
    print('Tarefa adicionada com sucesso!')
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
     print('*' * 50)
     print(' ' * 15, 'LISTA DE TAREFAS')
     print('*' * 50)
     n = 1
     for tarefa in lista_de_tarefas:
            print(f'{n} - {tarefa}')
            n = n + 1

def deletar_tarefa(lista_de_tarefas, tarefa):
     lista_de_tarefas.pop((tarefa - 1))
     return lista_de_tarefas

def exibir_menu():
     print('Escolha uma opção: \n' \
          ' 1 - Insira nova tarefa \n' \
            ' 2 - Lista tarefas \n' \
                ' 3 - Deletar tarefa \n' \
                    ' 4 - Sair'
                    )

lista_de_tarefas = []
continuar = True

print("\n" * 2)
print(">>> SEJA BEM VINDO À SUA LISTA DE TAREFAS! <<<")
print("\n")

while continuar:
    exibir_menu()
    print("-" * 50)
    opcao = input('Insira o que deseja fazer: ')
    if opcao == '1':
        tarefa = input('Insira uma tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == '2':
         listar_tarefas(lista_de_tarefas)
    elif opcao == '3':
         tarefa = input('Insira o número da tarefa que deseja deletar: ')
         if not tarefa.isnumeric():
            print('Número inválido! Tente novamente.')
            print("\n")
         elif int(tarefa) > len(lista_de_tarefas):
            print('Número inválido! Tente novamente.')
            print("\n")
         elif int(tarefa) <= 0:
            print('Número inválido! Tente novamente.')
            print("\n")
         else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao == '4':
        continuar = False
    else:
        print('Opção invalida! Por favor, tente novamente.')

    print('\n')