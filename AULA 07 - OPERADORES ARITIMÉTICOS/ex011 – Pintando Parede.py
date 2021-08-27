# Aula 7 – Operadores Aritméticos

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá
## Cada litro de tinta pinta uma área de 2m²

largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
area = largura*altura
tinta = area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3}m².\nVocê vai precisar de {:.3} litros de tinta para pintar esta parede.'.format(largura, altura, area, tinta))
