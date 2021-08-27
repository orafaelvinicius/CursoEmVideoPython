# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 pessoas.
# No final do programa mostre:
# A média de idade do grupo
# O nome do HOMEM MAIS VELHO
# Quantas MULHERES tem MENOS DE 20 anos

# -- Variáveis de controle
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0

# -- Estruture o laço de leitura e condições
for pessoa in range(1, 5):
    print('------ {}ª PESSOA ------'.format(pessoa))
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [ M / F ]: ')).strip()
    somaidade += idade

    # - Homem mais velho
    if pessoa == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    # - Contar as mulheres
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

    # - Média
mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.1f} anos.'.format(mediaidade))

print('O nome do homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))