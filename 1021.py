"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1021 - Notas e Moedas
"""
# -*- coding: utf-8 -*-

a = b = c = d = e = f = 0
N = float(input())
notas = int(N)
moedas = N - notas

if notas != 0:
    if(notas>=100):
        a = int(notas/100)
        notas = notas - int(a*100)
    if(notas>=50):
        b = int(notas/50)
        notas = notas - int(b*50)
    if(notas>=20):
        c = int(notas/20)
        notas = notas - int(c*20)
    if(notas>=10):
        d = int(notas/10)
        notas = notas - int(d*10)
    if(notas>=5):
        e = int(notas/5)
        notas = notas - int(e*5)
    if(notas>=2):
        f = int(notas/2)
        notas = notas - int(f*2)

g = h = i = j = k = l = 0
moedas = int((moedas + notas)*100)

if moedas != 0:
    if(moedas>=100):
        g = int(moedas/100)
        moedas = moedas - int(g*100)
    if(moedas>=50):
        h = int(moedas/50)
        moedas = moedas - int(h*50)
    if(moedas>=25):
        i = int(moedas/25)
        moedas = moedas - int(i*25)
    if(moedas>=10):
        j = int(moedas/10)
        moedas = moedas - int(j*10)
    if(moedas>=5):
        k = int(moedas/5)
        moedas = moedas - int(k*5)
    if(moedas>=1):
        l = moedas

print('NOTAS:')
print(f'{a} nota(s) de R$ 100.00')
print(f'{b} nota(s) de R$ 50.00')
print(f'{c} nota(s) de R$ 20.00')
print(f'{d} nota(s) de R$ 10.00')
print(f'{e} nota(s) de R$ 5.00')
print(f'{f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{g} moeda(s) de R$ 1.00')
print(f'{h} moeda(s) de R$ 0.50')
print(f'{i} moeda(s) de R$ 0.25')
print(f'{j} moeda(s) de R$ 0.10')
print(f'{k} moeda(s) de R$ 0.05')
print(f'{l} moeda(s) de R$ 0.01')