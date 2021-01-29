"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1045 - Tipos de Triângulos
"""
# -*- coding: utf-8 -*-

pontos = list(map(float, input().split()))
A, B, C = sorted(pontos)[::-1]

if (A >= B + C) or (B >= A + C) or (C >= B + A):
    print('NAO FORMA TRIANGULO')
elif (A*A) == ((B*B) + (C*C)):
    print('TRIANGULO RETANGULO')
elif (A*A) > ((B*B) + (C*C)):
    print('TRIANGULO OBTUSANGULO')
elif (A*A) < ((B*B) + (C*C)):
    print('TRIANGULO ACUTANGULO')
if (A == B) and (B == C):
    print('TRIANGULO EQUILATERO')
elif (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
    print('TRIANGULO ISOSCELES')