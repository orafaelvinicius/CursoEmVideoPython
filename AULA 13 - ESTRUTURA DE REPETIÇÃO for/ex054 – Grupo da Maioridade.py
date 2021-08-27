# Crie um programa que leia o ANO DE NACIMENTO de 7 PESSOAS. No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas ja são de maior
# considere 21 anos como maior de idade

# -- Importe as bibliotecas
from datetime import date

# -- Variáveis de controle
totmaior = 0 #acumulador
totmenor = 0 #acumulador
atual = date.today().year

# -- Estruture o laço de leitura e condições
for pessoas in range(1, 8):
    nasc = int(input('Digite o nascimento da {}ª pessoa: '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))

