'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

# -- Método 1 (com módulo)
'''
from math import factorial
n = int(input('Digite o número para calcular o seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')
'''

# -- Modo tradicional
numero = int(input('Digite o número para calcular o seu fatorial: '))
contador = numero
fator = 1
print(f'Calculando {contador}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fator *= contador
    contador -= 1
print(f'{fator}.')
