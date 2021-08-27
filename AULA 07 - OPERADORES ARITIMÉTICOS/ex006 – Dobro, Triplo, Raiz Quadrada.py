# Aula 7 – Operadores Aritméticos

# Faça um programa que leia um número inteiro e mostre na tela o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} é {}, já o tríplo é {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, d, t, n, r))

# Você pode colocar todas as variáveis dentro do print que também funciona

# A função "pow()" também é usado para calcular a raiz quadrada
