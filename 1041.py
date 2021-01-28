"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1041 - Coordenadas de um ponto
"""
# -*- coding: utf-8 -*-

x, y = input().split()

x = float(x)
y = float(y)

if x == 0.0:
    if y == 0.0:
        print('Origem')
    else:
        print('Eixo Y')
elif y == 0.0:
    print('Eixo X')
elif x > 0.0:
    if y > 0.0:
        print('Q1')
    else: 
        print('Q4')
elif x < 0.0:
    if y > 0.0:
        print('Q2')
    else:
        print('Q3')