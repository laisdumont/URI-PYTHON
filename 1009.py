"""
    Autora: laisdumont
    Data: 23/01/21
    Desafio: 1009 - Salário com Bônus
"""
# -*- coding: utf-8 -*-

nome = str(input())
sfixo = float(input())
vendas = float(input())

stotal = vendas*0.15 + sfixo

print(f'TOTAL = R$ {stotal:.2f}')