# Faça um programa que leia o peso de 5 pessoas e no final mostre o MAIOR e o MENOR peso lido

# -- Auxiliares
maior = 0
menor = 0

# -- O programa
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: Kg'.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
