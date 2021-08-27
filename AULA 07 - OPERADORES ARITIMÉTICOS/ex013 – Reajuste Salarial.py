# Aula 7 – Operadores Aritméticos

# Faça um algorítimo que leia o salário de um funcionário e mostre seu novo valor com 15% de aumento

salario = float(input('Qual o seu salário? R$'))
aumento = salario + (salario * 15 / 100)
print('Um funcionário com salário de R${:.2f}, com um aumento de 15% passará a receber R${:.2f}'.format(salario, aumento))
