# Aula 7 – Operadores Aritméticos

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela teria
## considere o dolar a R$3,27 ou busque na net

c = float(input('Quanto você tem em R$? '))
d = c/4.97
e = c/5.93

print('Os seus BRL {:.2} podem comprar\nUSD {:.2}\nEUR {:.2}'.format(c,d,e))
