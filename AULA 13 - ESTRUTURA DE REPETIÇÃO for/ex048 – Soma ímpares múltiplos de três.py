# Faça um programa que calcule a soma entre TODOS OS NÚMERO ÍMPARES que são MULTIPLOS DE 3 e que estão no intervadlo de 1 até 500.

soma = 0 # acumulador
cont = 0 # contator
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma = soma + impar # ou use soma += impar
        cont = cont + 1     # ou use cont += 1
print('A soma de todos os {} números encontrados é igual a {}.'.format(cont, soma))
