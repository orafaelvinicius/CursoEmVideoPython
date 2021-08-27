# Faça um programa que mostre na tela uma contagem regressima para o estouro de fogos de artifícios, indo de 10 até 0, com pausa de 1 segund entre eles.

# -- Importando bibliotecas
from time import sleep

# -- Laço para contagem regressiva
for f in range(10, -1, -1):
    sleep(1)
    print(f)
print('BOOOM!!')