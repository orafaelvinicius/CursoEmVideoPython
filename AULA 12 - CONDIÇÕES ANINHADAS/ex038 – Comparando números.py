# Comparando números
# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

# -- Lendo os números
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

# -- Condições
if a > b:
    print('O PRIMEIRO número é maior.')
elif b > a:
    print('O SEGUNDO número é maior')
else:
    print('Os números SÂO IGUAIS')
