# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME.

nome = input('Digite seu nome completo: ').strip().upper()

print('Seu nome tem Silva? {}.'.format('SILVA' in nome))
