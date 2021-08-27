# Aula 7 – Operadores Aritméticos

# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preço = float(input('Qual o preço do produto? R$'))
desconto = preço - (preço * 5 / 100)
print('O valor do produto é R${:.2f}, com 5% de desconto, passará a ser R${:.2f}'.format(preço, desconto))
