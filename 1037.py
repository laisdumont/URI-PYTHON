"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1037 - Intervalo
"""
# -*- coding: utf-8 -*-

num = float(input())
resp = ''

if 0 <= num <= 25:
    resp = 'Intervalo [0,25]'
elif 25 < num <= 50:
    resp = 'Intervalo (25,50]'
elif 50 < num <= 75:
    resp = 'Intervalo (50,75]'
elif 75 < num <= 100:
    resp = 'Intervalo (75,100]'
else:
    resp = 'Fora de intervalo'
    
print(resp)