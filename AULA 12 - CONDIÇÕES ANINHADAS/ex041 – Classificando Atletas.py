# Classificando Atletas
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

#-- Importando as bibliotecas necessárias
from time import sleep
from datetime import date

#-- Lendo o ano do nascimento dos atletas
nasc = int(input('Qual o ano do seu nascimento? '))
atual = date.today().year
idade = atual - nasc

print('*-'*20)
print('Verificando a sua categoria...')
print('*-'*20)
sleep(1)

#-- Condições para categoria por idade
if idade <= 9:
    print('Quem tem {} anos, está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Quem tem {} anos, está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Quem tem {} anos, está na categoria JÚNIOR'.format(idade))
elif idade <= 25:
    print('Quem tem {} anos, está na categoria SÊNIOR'.format(idade))
elif idade > 25:
    print('Quem tem {} anos, está na categoria MASTER'.format(idade))
else:
    print('Erro! Tente novamente.')

