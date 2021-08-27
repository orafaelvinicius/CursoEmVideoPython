# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que foram PARES. Se o número digitado for ÍMPAR, desconsidere-o.

# -- Insira um acumulador e contador
soma = 0 #->acumulador
cont = 0 #->contador

# -- Regras da atividade
for n in range(1, 7):
    num = int(input('Digite o {}ª valor: '.format(n)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
    else:
        pass

print('A soma de todos os {} números PARES digitados é igual a {}.'.format(cont, soma))
