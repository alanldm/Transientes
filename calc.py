def t_l(zl, z0):
    return (zl-z0)/(zl+z0)

def t_s(zs, z0):
    return (zs-z0)/(zs+z0)
    
def v_0(vs, z0, zs):
    return (z0*vs)/(z0+zs)

def v_l(vs, z0, zl):
    return (zl*vs)/(zl+z0)

def time(l, up):
    return l/up

'''
ci -> Tensão inicial na saída da fonte
i -> Tempo onde se observa a primeira mudança
f -> Tempo final
p -> Passo de tempo em tempo, baseado no ponto onde se observa as mudanças
t -> Tempo para se percorrer de uma ponta a outra
tl -> Índice de reflexão na carga
ts -> Índice de reflexão na fonte
'''

def calc_ten(ci, i, f, p, t, tl, ts):
    tensoes = []
    tempos = []
    tensao_nova = 0    
    tensao = 0
    fator = 1
    lado = False
    for j in range(0,f,i):
        if j%t==0:
            if lado==True:
                fator = fator*tl
                tensao_nova = tensao + ci*fator
                lado = False
            else:
                if j!=0:
                    fator = fator*ts
                    tensao_nova = tensao + ci*fator
                    lado = True
                else:
                    tensao_nova = ci
                    lado = True
        if j==i:
            tempos.append(j)
            tempos.append(j)
            tensoes.append(tensao)
            tensoes.append(tensao_nova)
            tensao = tensao_nova
            i += p
        else:
            tempos.append(j)
            tensoes.append(tensao)

    return [tempos, tensoes] 
