"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1010 - Cálculo Simples
"""
# -*- coding: utf-8 -*-

cp1, np1, vp1 = str(input()).split(' ')
cp2, np2, vp2 = str(input()).split(' ')

cp1 = int(cp1)
np1 = int(np1)
vp1 = float(vp1)

cp2 = int(cp2)
np2 = int(np2)
vp2 = float(vp2)

valor = (np1*vp1) + (np2*vp2)

print(f'VALOR A PAGAR: R$ {valor:.2f}')