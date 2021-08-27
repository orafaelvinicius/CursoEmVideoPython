# Alistamento Militar
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# -- Importe as bibliotecas necessárias
from datetime import date

print('+-'*30)
print('SEJA BEM VINDO AO SERVIÇO DE ALISTAMENTO OBRIGATÓRIO')
print('+-'*30)
# -- Lendo a idade
nasc = int(input('Qual o ano que você nasceu? '))
atual = date.today().year
idade = atual - nasc
print('Você tem {} anos em {}'.format(idade, atual))
print('''Digite [ H ] se você for HOMEM.
Digite [ M ] se vocÊ for MULHER''')
sexo = str(input('Selecione o seu sexo: ')).strip().upper()

# -- Condições de alistamento
if sexo == 'M':
    print('SEU ALISTAMENTO NÃO É OBRIGATÓRIO')

elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
