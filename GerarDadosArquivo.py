from re import findall

gramatica = dict()
with open('gramatica_exemplo.txt', 'r') as file:
    for lin in file.readlines():
        #utilizando um Regex(Regular expression)
        prox = findall(r'[a-zA-Z]+\s\=\>', lin)[0]
        chave = prox.replace('=>', '').strip()
        variaveis = lin.replace(prox, '').strip().split('|')
        gramatica[chave] = variaveis





