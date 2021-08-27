# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo pc.
# O programa deverá escrever se o usuário venceu ou perdeu

# ---------- JOGO DE ADIVINHAÇÃO v1.0 ----------------


from random import randint
from time import sleep

pc = randint(0, 5) # Comando para fazer o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número que pensei? ')) # Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(2)

if jogador == pc:
    print('PARABÉNS, VOCÊ VENCEU!')
else:
    print('Ganhei!! Eu pensei no número {} e não no número {}!'.format(pc, jogador))



