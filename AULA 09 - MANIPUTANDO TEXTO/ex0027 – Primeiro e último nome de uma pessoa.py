# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE

## Ex: Ana Maria de Souza
## Primeiro: Ana
## ÚLTIMO: ALBUQUERQUE

n = str(input('Digite o seu nome completo: ')).strip().upper()
nome = n.split()

print('Seu nome completo é: {}.'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
