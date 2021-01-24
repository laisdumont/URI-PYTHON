"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1018 - Cédulas
"""
# -*- coding: utf-8 -*-

a = b = c = d = e = f = g = 0
valor = int(input())
n = valor

if(n>=100):
    a = int(n/100)
    n = n - int(a*100)
if(valor>=50):
    b = int(n/50)
    n = n - int(b*50)
if(valor>=20):
    c = int(n/20)
    n = n - int(c*20)
if(valor>=10):
    d = int(n/10)
    n = n - int(d*10)
if(valor>=5):
    e = int(n/5)
    n = n - int(e*5)
if(valor>=2):
    f = int(n/2)
    n = n - int(f*2)
if(valor>=1):
    g = int(n/1)
    
print(valor)
print(f'{a} nota(s) de R$ 100,00')
print(f'{b} nota(s) de R$ 50,00')
print(f'{c} nota(s) de R$ 20,00')
print(f'{d} nota(s) de R$ 10,00')
print(f'{e} nota(s) de R$ 5,00')
print(f'{f} nota(s) de R$ 2,00')
print(f'{g} nota(s) de R$ 1,00')