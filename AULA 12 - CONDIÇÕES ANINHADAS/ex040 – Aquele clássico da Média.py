# Aquele clássico da Média
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

# -- Coletando notas e média
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
print('A média entre as notas {} e {} é {}.'.format(n1, n2, media))

# -- Condições
if 7 > media >= 5:
    print('Sua nota não foi lá das melhores. Você está em RECUPERAÇÃO.')
elif media < 5:
    print('Sua nota está abaixo da média, você está REPROVADO.')
elif media >= 7:
    print('Parabéns, você está APROVADO!')
