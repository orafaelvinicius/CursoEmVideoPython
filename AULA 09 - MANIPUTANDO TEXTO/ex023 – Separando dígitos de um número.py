# FAÇA UM PRGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADOS
## Ex: Digitie um número: 1834
### unidade: 4
### dezena: 3
### centena: 8
### milhar: 1

numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('Analsiando o número {} tem: '.format(numero))
print('{} unidades'.format(unidade))
print('{} dezenas'.format(dezena))
print('{} cemtemas'.format(centena))
print('{} milhares'.format(milhar))
