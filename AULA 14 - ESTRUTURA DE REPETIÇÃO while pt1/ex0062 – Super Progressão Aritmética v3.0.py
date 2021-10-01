# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Utilize o "0" nas 2 variáveis para sair')
print('''\033[33m
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
         GERADOR DE PA 
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\033[m''')


primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
contador = 1 # conta quntos termos serão utilziados começando em 1
total = 0 # termo de início da contagem da repetição
mais = 10 # variável inicial para a exibição dos 10 primeiros termos

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = print('\033[33m Quantos termos você ainda quer mostrar?\033[m')

print('FIM')

