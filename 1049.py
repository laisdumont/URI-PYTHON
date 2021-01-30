"""
    Autora: laisdumont
    Data: 30/01/21
    Desafio: 1049 - Animal
"""
# -*- coding: utf-8 -*-

t1 = str(input()).upper()
t2 = str(input()).upper()
t3 = str(input()).upper()

if t1 == 'VERTEBRADO':
    if t2 == 'AVE':
        if t3 == 'CARNIVORO':
            animal = 'aguia'
        else:
            animal = 'pomba'
    else:
        if t3 == 'ONIVORO':
            animal = 'homem'
        else:
            animal = 'vaca'
else:
    if t2 == 'INSETO':
        if t3 == 'HEMATOFAGO':
            animal = 'pulga'
        else:
            animal = 'lagarta'
    else:
        if t3 == 'HEMATOFAGO':
            animal = 'sanguessuga'
        else:
            animal = 'minhoca'

print(animal)