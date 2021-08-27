# Aula 7 – Operadores Aritméticos

# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada

n = int(input('DIGITE UM NÚMERO PARA VER SUA TABUADA: '))
n1 = n*1
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
print('-' *12)
print('De 1 é {}\nDe 2 é {}\nDe 3 é {}\nDe 4 é {}\nDe 5 é {}\nDe 6 é {}\nDe é 7 {}\nDe 8 é {}\nDe 9 é {}'.format(n1,n2,n3,n4,n5,n6,n7,n8,n9))
print('-'*12)

# ou use o comando:
# print('{} x {:2} = {}'.format(n, 1, n*1))
# print('{} x {:2} = {}'.format(n, 1, n*2))
# print('{} x {:2} = {}'.format(n, 1, n*3))
# print('{} x {:2} = {}'.format(n, 1, n*4))
# print('{} x {:2} = {}'.format(n, 1, n*5))
# ...