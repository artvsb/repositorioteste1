import os
opcao_escolhida = int(input('Escolha uma opção: '))

def alt1():
    os.system ('cls')
    print('Encerrando o programa...')
match opcao_escolhida:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
       alt1()