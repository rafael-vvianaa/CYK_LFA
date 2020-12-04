from re import findall
gramatica = dict()

with open('gramatica.txt', 'r') as file:
    for lin in file.readlines():
        prox = findall(r'[a-zA-Z]+\s\=\>', lin)[0]
        chave = prox.replace('=>', '').strip()
        productions = lin.replace(prox, '').strip().split('|')
        gramatica[chave] = productions
