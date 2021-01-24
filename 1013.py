"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1013 - O maior
"""
# -*- coding: utf-8 -*-

A, B, C = str(input()).split(' ')

A = int(A)
B = int(B)
C = int(C)

lista = [A, B, C]

print(f'{max(lista)} eh o maior')