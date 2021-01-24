"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1017 - Gasto de Combustível
"""
# -*- coding: utf-8 -*-

tempo = int(input())
vmedia = int(input())

dist = tempo*vmedia
litros = dist/12

print(f'{litros:.3f}')