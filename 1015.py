"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1015 - Distância entre 2 pontos
"""
# -*- coding: utf-8 -*-

from math import sqrt

x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))

Distância = sqrt(pow(x2-x1, 2) + pow(y2-y1 ,2))

print(f'{Distância:.4f}')