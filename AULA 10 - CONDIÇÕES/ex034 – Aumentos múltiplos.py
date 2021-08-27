# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# para salários SUPERIOR a R$1200, calcule um aumento de 10%
# para salários INFERIOR ou iguais, o aumento deve ser de 15%

salario = float(input('Qual o salário do funcionário? R$'))

if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))
