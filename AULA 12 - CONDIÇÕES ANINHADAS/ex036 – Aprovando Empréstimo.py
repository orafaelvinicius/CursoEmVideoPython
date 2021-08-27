# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
prazo = int(input('Em quantos anos você vai pagar? '))

#-- Calculando a prestção
prestacao = casa / (prazo * 12)
minimo = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, prazo), end='')
print(' a prestação será de R${:.2f}.'.format(prestacao))

if prestacao <= minimo:
    print('O empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO.')
