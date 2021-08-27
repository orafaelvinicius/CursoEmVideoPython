# Faça um programa que leia um número inteiro e diga se ele é ou não um NÚMERO PRIMO (divisível por 1 ou por ele mesmo)

# -- Coletando os números
num = int(input('Digite um número: '))
tot = 0 #contador
# -- Laço para número primo
for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1 #contador
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')

print('\n\033[mO número {} foi divisível {} vezes.'.format(c, tot))

# -- condição para número primo
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

