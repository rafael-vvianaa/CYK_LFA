from CYK_main import palavra

matriz = [list() for i in range(len(palavra))]
palavra = list(palavra)

def regraMatriz( matriz, lin, palavra, gramatica):
    base = matriz[len(matriz) - 1]
    if (len(base) != 0):
        if list(gramatica.chaves())[0] in base[0]:
            print('\033[32mA palavra é reconhecida pela gramática!\033[m')
        else:
            print('\033[32mA palavra não é reconhecida pela gramática!\033[m')
        return matriz
        combinacoes = x(palavra, lin)

        if len(combinacoes[0]) > 2:

