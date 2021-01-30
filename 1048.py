"""
    Autora: laisdumont
    Data: 29/01/21
    Desafio: 1048 - Aumento de Salário
"""
# -*- coding: utf-8 -*-

sal = float(input())

if 0.00 <= sal <= 400.00:
    novo_sal = sal + sal*0.15
    reajuste = sal*0.15
    percentual = 15
elif 400.00 < sal <= 800.00:
    novo_sal = sal + sal*0.12
    reajuste = sal*0.12
    percentual = 12
elif 800.00 < sal <= 1200.00:
    novo_sal = sal + sal*0.10
    reajuste = sal*0.10
    percentual = 10
elif 1200.00 < sal <= 2000.00:
    novo_sal = sal + sal*0.07
    reajuste = sal*0.07
    percentual = 7
elif sal > 2000.00:
    novo_sal = sal + sal*0.04
    reajuste = sal*0.04
    percentual = 4

print(f'Novo salario: {novo_sal:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')