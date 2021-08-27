# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# insira os nomes
from random import shuffle ## OU apenas 'import radom' para importar a biblioteca toda.

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
# faça uma lista de alunos
alunos = [a1, a2, a3, a4]
# faça o sorteio (shuffler = embaralhar)
shuffle(alunos)

print('A ordem de apresentação será {}'.format(alunos))
