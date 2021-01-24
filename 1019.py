"""
    Autora: laisdumont
    Data: 23/01/21
    Desafio: 1019 - Conversão de Tempo
"""
# -*- coding: utf-8 -*-

tempo = int(input())
h = m = s = 0

if tempo >= 3600:
    h = int(tempo/3600)
    tempo = tempo - h*3600
if tempo >= 60:
    m = int(tempo/60)
    tempo = tempo - m*60
if tempo < 60:
    s = tempo
    
print(f'{h}:{m}:{s}')
    