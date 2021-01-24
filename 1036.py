"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1036 - Fórmula de Bhaskara
"""
# -*- coding: utf-8 -*-

from math import sqrt

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

delta = (B**2) - (4*A*C)

if A == 0 or delta < 0:
    print('Impossivel calcular')
else:
    raizdelta = sqrt(delta)
    r1 = (-B + raizdelta)/(2*A)
    r2 = (-B - raizdelta)/(2*A)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')