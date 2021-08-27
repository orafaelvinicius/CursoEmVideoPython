# Aula 6 - Tipos primitivos (int 'inteiros', float 'flutuantes/rais', bool 'True ou False', str 'strengs/valores')
## Você pode descobrir o tipo de uma vaviável inserindo a função 'type' no print.
# Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2

print('A soma entre {} e {} é igual a {}.'.format(n1,n2,s))
