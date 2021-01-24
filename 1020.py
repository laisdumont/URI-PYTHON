"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1020 - Idade em Dias
"""
# -*- coding: utf-8 -*-

a = m = d = 0
idade = int(input())

if idade >= 365:
    a = int(idade/365)
    idade = idade - a*365
if idade >= 30:
    m = int(idade/30)
    idade = idade - m*30
if idade < 30:
    d = idade
    
print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{d} dia(s)')