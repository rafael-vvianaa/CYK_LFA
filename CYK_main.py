from lib.interface.interface import *
from time import sleep

while True:
    resposta = menu(['Digite a Palavra','Sair do Sistema'])
    if resposta == 1:
       print('Opcao1')
    elif resposta == 2:
       print('opcao 2')
       break
    else:
        print('\033Error, por favor digite uma opção válida!\033[m')
    sleep(2)
