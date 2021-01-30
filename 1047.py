"""
    Autora: laisdumont
    Data: 29/01/21
    Desafio: 1047 - Tempo do Jogo com Minutos
"""
# -*- coding: utf-8 -*-

hi, mi, hf, mf = list(map(int, input().split()))

hmi = hi*60 + mi
hmf = hf*60 + mf

if hmi == hmf:
    h = 24
    m = 0
elif hmi < hmf:
    h = int((hmf - hmi)/60)
    m = (hmf - hmi)%60
else: 
    h = int((1440 - hmi + hmf)/60)
    m = (1440 - hmi + hmf)%60
    
print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)') 