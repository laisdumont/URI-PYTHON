"""
    Autora: laisdumont
    Data: 29/01/21
    Desafio: 1046 - Tempo do Jogo
"""
# -*- coding: utf-8 -*-

Hi, Hf = list(map(int, input().split()))

if Hi == Hf:
    horas = 24
elif Hi > Hf:
    horas = 24 - Hi + Hf
else:
    horas = Hf - Hi

print(f'O JOGO DUROU {horas} HORA(S)')