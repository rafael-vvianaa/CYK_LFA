from Regras import verificacao
from Regras import geracao
from Regras import noh
from lib.interface.interface import *
from time import sleep
from GerarDadosArquivo import gramatica
from math import floor, ceil



while True:
    resposta = menu(['Caso queria digitar uma palavra','Sair do Sistema'])
    if resposta == 1:
       palavra = input('Digite a Palavra a ser verificada: ')
       matriz = [list() for s in range(len(palavra))]
       palavra = list(palavra)


       def main(palavra, gramatica, matriz, lin):
           init = matriz[len(matriz) - 1]
           if (len(init) != 0):
               if list(gramatica.keys())[0] in init[0]:
                   print('\033[31mPalavra digitada faz parte da gramatica.\033[m')
               else:
                   print('\033[31mPalavra digitada não faz parte da gramatica.\033[m')
               return matriz

           var_comb = geracao(palavra, lin)

           if len(var_comb[0]) > 2:
               for s, tudo in enumerate(var_comb):
                   var_comb[s] = []
                   for d in range(len(tudo) - 1):
                       var_comb[s].append([tudo[:d + 1], tudo[d + 1:]])

           for tudo in var_comb:
               if type(tudo[0]) is list:
                   calcular = list()

                   for d in tudo:
                       checar = []
                       for e in d:
                           if len(e) > 1:
                               t = ''.join(palavra)
                               joinar = ''.join(e)
                               posicao = t.find(joinar)
                               var_no = matriz[len(joinar) - 1][posicao]
                               checar.append(var_no)
                           else:
                               var_no = verificacao(e, gramatica)
                               checar.append(var_no)
                       checar = noh(checar[0], checar[1])
                       resultado = verificacao(checar, gramatica)
                       calcular.append(resultado)

                   procurar = ''
                   for x in calcular:
                       procurar += x
                   matriz[lin].append(procurar)
               else:

                   var_no = verificacao(tudo, gramatica)
                   if len(var_no) > 1:
                       checar = noh(var_no[:ceil(
                           len(var_no) / 2)], var_no[ceil(len(var_no) / 2):])
                       checar = list(dict.fromkeys(checar))
                       resultado = verificacao(checar, gramatica)
                       if resultado == '':
                           resultado = var_no
                       matriz[lin].append(resultado)
                   else:
                       matriz[lin].append(var_no)

           lin += 1
           return main(palavra, gramatica, matriz, lin)
       resultado = main(palavra, gramatica, matriz, 0)


    elif resposta == 2:
       print('Finalizando...')
       break
    else:
        print('\033[31mErro, por favor digite uma opção válida!\033[m')
    sleep(1)
