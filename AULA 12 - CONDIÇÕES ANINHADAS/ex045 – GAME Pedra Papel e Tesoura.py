#  Crie um programa que faça o computador jogar Jokenpô com você.

# -- Importando as bibliotecas necessárias
from random import randint
from time import sleep

# -- Coletando a opção dos jogadores
print('{:=^10}'.format(' VAMOS JOGAR '))
jogador = int(input('''[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura
Esolha uma das opções acima:'''))

pc = randint(0, 2)
sleep(1)

# -- O jogo
itens = ('Pedra', 'Papel', 'Tesoura')

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!')
sleep(0.5)

print('-='* 20)
print('O computador escolheu {}.'.format(itens[pc]))
print('O jogador escolheu {}.'.format(itens[jogador]))
print('-='* 20)

# -- Condições do jogo
if pc == 0: # PC jogou PEDRA
    if jogador == 0: # Jogador jogou PEDRA
        print('EMPATOU. Jogue novamente!')
    elif jogador == 1: # Jogador jogou PAPEL
        print('O JOGADOR VENCEU!')
    elif jogador == 2: # Jogador jogou TESOURA
        print('O COMPUTADOR VENCEU! Jogue novamente.')
    else:
        print('Jogada inválida.')

elif pc == 1: # PC jogou PAPEL
    if jogador == 0: # Jogador jogou PEDRA
        print('O COMPUTADOR VENCEU! Jogue novamente.')
    elif jogador == 1: # Jogador jogou PAPEL
        print('EMPATOU. Jogue novamente!')
    elif jogador == 2: # Jogador jogou TESOURA
        print('O JOGADOR VENCEU!')
    else:
        print('Jogada inválida.')

elif pc == 2: # PC jogou TESOURA
    if jogador == 0: # Jogador jogou PEDRA
        print('O JOGADOR VENCEU!')
    elif jogador == 1: # Jogador jogou PAPEL
        print('O COMPUTADOR VENCEU! Jogue novamente.')
    elif jogador == 2: # Jogador jogou TESOURA
        print('EMPATOU. Jogue novamente!')
    else:
        print('Jogada inválida.')
