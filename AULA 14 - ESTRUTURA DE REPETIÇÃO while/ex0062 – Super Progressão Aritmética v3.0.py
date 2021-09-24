# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('GERADOR DE PA (até o 10º termo)')
print('-=' * 10)

termo = 1

while termo != 0:
    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Razão da PA: '))
    termo = primeiro
    contador = 1 #quantos termos foram começando em 1

    while contador <= 10:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1

    print('FIM DA CONTAGEM')
print('\033[33mFIM DO PROGRAMA\033[m')
