# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite o ângulo desejado: '))
se = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo é: {}\nO seno é: {:.2f}\nO cosseno é: {:.2f}\nE a tangente é: {:.2f}'.format(ang, se, cos, tang))
