
"""
    Autora: laisdumont
    Data: 30/01/21
    Desafio: 1051 - Imposto de Renda
"""
# -*- coding: utf-8 -*-

sal = float(input())

if 2000.00 < sal <= 3000.00:
    imp = (sal - 2000)*0.08
    print(f'R$ {imp:.2f}')
elif 3000.00 < sal <= 4500.00:
    imp = (1000*0.08) + ((sal-3000)*0.18)
    print(f'R$ {imp:.2f}')
elif sal > 4500.00:
    imp = (1000*0.08) + (1500*0.18) + ((sal-4500)*0.28)
    print(f'R$ {imp:.2f}')

if sal <= 2000.00:
    print('Isento')