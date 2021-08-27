# Aula 7 – Operadores Aritméticos

# A ordem de precedência é extremamente importante

# Operadores aritiméticos (Binário): +, -, *, /, ==, **(espoente), //(divisão inteira), %

# Ordem de precedeência
# 1º: ()
# 2º: **
# 3º: *, /, //, %
# 4º: +, -

# nome = input('Qual é seu nome?')
# print('É um prazer te conhecer, {:=^20}.'.format(nome))
#Use "{:simbolo20}" para definir espaços dentro do print. < alinha para a direita, > alinha para esqueda, ^ centrazila o texto
## Você também pode colocar qualquer caractere logo após a ":" e antes do simbolo para preencher os espaços com o caractere escolhido

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro númnero: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma vale {}, a multiplicação vale {}, a divisão é {}'.format(s, m, d))
print(' a divisão inteira é {} e a é {}.\n'.format(di , e), end=' FIM ')
