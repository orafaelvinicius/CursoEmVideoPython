# Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA (progressão aritimética). No final, mostre os 10 PRIMEIROS termos dessa progressão
# (PA = contagem do número pulando de x números)

print('='*20)
print('10 TERMOS DA PA')
print('='*20)

# -- Inserindo um contador
cont = 0

# -- Lendo o primeiro termo
num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1) * razao #- Formula para descobrir o enézimo termo da PA

# -- Estrutura de repetição
for p in range(num, decimo + razao, razao):
    print('{}'.format(p), end=' -> ')
print('Acabou')