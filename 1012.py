"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1012 - Área
"""
# -*- coding: utf-8 -*-

A, B, C = str(input()).split(' ')

A = float(A)
B = float(B)
C = float(C)

print(f'TRIANGULO: {((A*C)/2):.3f}')
print(f'CIRCULO: {(3.14159*pow(C, 2)):.3f}')
print(f'TRAPEZIO: {((C*(A+B))/2):.3f}')
print(f'QUADRADO: {(B*B):.3f}')
print(f'RETANGULO: {(A*B):.3f}')