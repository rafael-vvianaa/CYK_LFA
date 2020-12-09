
def verificacao(t, gramatica):
    varP = ''
    if (type(t) is list):
        for s in t:
            varP += verificacao(s, gramatica)
    else:
        for chave, x in gramatica.items():
            if t in x:
                varP += chave
    return varP


def geracao(t, lin):
    passo = lin + 1
    var_comb = []
    for s in range(len(t)):
        simbolo = []
        try:
            if (lin > 0):
                for d in range(s, passo + s):
                    simbolo.append(t[d])
                var_comb.append(simbolo)
            else:
                var_comb.append(t[s:passo][0])
                passo += 1
        except:
            pass
    return var_comb


def noh(ve, node):
    var_dt = []
    for s in ve:
        for varN in node:
            var_dt.append(f'{s}{varN}')
    return var_dt



