# Crie um programa que leia um número inteiro qualquer e mostre na tela se esse número é PAR ou ÍMPAR.

# ---------- Lendo um número inteiro
num = int(input('Digite um número qualquer: '))
#print('Seu número é {}'.format(num))

# ---------- Par ou ímpar?
res = num % 2

if res == 0:
    print('O número {} é um número par'.format(num))
else:
    print('O número {} é um número ímpar'.format(num))
