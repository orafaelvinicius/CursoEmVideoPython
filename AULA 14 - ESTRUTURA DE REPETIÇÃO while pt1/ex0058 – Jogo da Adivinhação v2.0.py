# Melhore o jogo do ex0028 onde o computar vai "pensar" em um NÚMERO ENTRE 0 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostre no final quantos palpites foram necessários para acertar

# ---------- JOGO DE ADIVINHAÇÃO v2.0 ----------------

from random import randint

# -- Pensando no número
pc = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

# -- Estrututra de repetição
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Pensei em um número MAIOR. Tente novamente')
        elif jogador > pc:
            print('Pensei em um número MENOR. Tente novamente')

print(f'PARABÉNS, VOCÊ VENCEU!\nVocê precisou de apenas {palpite} tentativas para me vencer.')


