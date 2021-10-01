# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA (até o 10º termo)')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1 #quantos termos foram começando em 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1

print('FIM DA CONTAGEM')
