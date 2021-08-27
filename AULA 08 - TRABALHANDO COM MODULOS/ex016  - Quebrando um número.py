# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER DO TECLADO E MOSTRE SEU NÚMERO INTERIO

from math import trunc
num = float(input(('DIGITE UM NÚMERO QUALQUER: ')))
print('O número digitado foi {}, a porção inteira deste número é: {}'.format(num, trunc(num))) ##Se importou a biblioteca inteira, use "mat.trunc' ou biblioteca.função
