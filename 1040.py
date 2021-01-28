"""
    Autora: laisdumont
    Data: 24/01/21
    Desafio: 1040 - Média 3
"""
# -*- coding: utf-8 -*-

N1, N2, N3, N4 = input().split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = (N1*2 + N2*3 + N3*4 + N4)/10

if media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
    
elif media < 5.0:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
    
elif 5.0 <= media <= 6.9:
    nota_exame = float(input())
    media_final = (media + nota_exame)/2
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {nota_exame:.1f}')
    
    if media_final >= 5.0:
        print('Aluno aprovado.')
        
    if media_final <= 4.9:
        print('Aluno reprovado.')
        
    print(f'Media final: {media_final:.1f}')
