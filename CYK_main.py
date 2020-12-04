from lib.interface.interface import *
from time import sleep

while True:
    resposta = menu(['Digite uma Palavra','Sair do Sistema'])
    if resposta == 1:
       print('Opcao1')
    elif resposta == 2:
       print('Finalizando...')
       break
    else:
        print('\033[31mErro, por favor digite uma opção válida!\033[m')
    sleep(2)
