# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot ## ou use apenas 'import math' para importar a biblioteca interrira

co = float(input('COMPRIMENTO DO CATETO OPOSTO: '))
ca = float(input('COMPRIMENTO DO CATETO ADJACENTE: '))
hi = hypot(co, ca)
print('A hiportenusa vai medir {:.2f}'.format(hi))