"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1038 - Lanche
"""
# -*- coding: utf-8 -*-

cod, qnt = input().split()

cod = int(cod)
qnt = float(qnt)

if cod == 1:
    total = 4 * qnt
elif cod == 2:
    total = 4.5 * qnt
elif cod == 3:
    total = 5 * qnt
elif cod == 4:
    total = 2 * qnt
elif cod == 5:
    total = 1.5 * qnt

print(f'Total: R$ {total:.2f}')