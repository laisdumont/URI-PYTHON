"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1044 - Múltiplos
"""
# -*- coding: utf-8 -*-

A, B = list(map(int, input().split()))

if (A % B == 0) or (B % A == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')