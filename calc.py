import matplotlib.pyplot as plt
import numpy as np

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

z0 = 75
zl = 125
zs = 25
vs = 4
up = 0.1*300000000
l = 0.06

v0 = v_0(vs, z0, zs)
vl = v_l(vs, z0, zl)
t = time(l, up)
tl = t_l(zl, z0)
ts = t_s(zs, z0)

print(f"Tensão inicial (v0) = {v0}V")
print(f"Tensão esperada na saída (vl) = {vl}V")
print(f"Tempo para se percorrer a linha (t) = {t}ns")
print(f"Índice de reflexão na carga (tl) = {tl}")
print(f"Índice de reflexão na saída da fonte (ts) = {ts}")

resultado = calc_ten(v0, 1, 9, 2, 2, tl, ts)

for i in range(0, len(resultado[0])):
    print(f"{resultado[0][i]}            {resultado[1][i]}")

plt.plot(resultado[0], resultado[1])
plt.show()