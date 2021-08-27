# Analisando Triângulos v2.0
## Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

#DESAFIO 35
print('=-'*20)
print('Analisador de triângulos')
print('=-'*20)
r1 = float(input('Qual o primeiro seguimento? '))
r2 = float(input('Qual o segundo seguimento? '))
r3 = float(input('Qual o terceiro seguimento? '))

#-- Verificando os seguimentos
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo ', end='') # Use o 'end='' para não pular a linha do print
    # estrutura de aninhamento de if dentro de if.
    if r1 == r2 and r2 == r3 and r3 == r1: #outra forma de fazer: if r1 == r2 == r3
        print('EQUILÁTERO!')
    if r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo.')
