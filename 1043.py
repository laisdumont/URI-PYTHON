"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1043 - Triângulo
"""
# -*- coding: utf-8 -*-

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

if (A < B + C) and (B < A + C) and (C < A + B):
    Per = A + B + C
    print(f'Perimetro = {Per:.1f}')
else:
    Area = ((A+B)*C)/2
    print(f'Area = {Area:.1f}')