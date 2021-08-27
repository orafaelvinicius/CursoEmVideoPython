# Escreva um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digitie o primeiro valor: '))
b = int(input('Digitie o segundo valor: '))
c = int(input('Digitie o terceiro valor: '))

# -- Verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# -- Verificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
