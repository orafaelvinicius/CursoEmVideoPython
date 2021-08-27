#### CONDIÇÕES
### Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

## Condições simples
# Os comando de inicio e fim são os mesmos. Ou seja, você pode criar 1 único programa com 2 ou mais fluxos
# Uma condição simples é o "SE" e o "SENÃO", comandos bem parecidos com a sintaxe do excel por exemplo.
# A estrutura (ou INDENTAÇÃO) dirá qual será a sequência de execução do seu programa divido por BLOCOS VERDADEIROS E FALSOS

#ex de estrutura condicional: (TROQUE O "SE" por if: e o "SENÃO" por else:
# if carro.esquerda()
#   bloco _True_
# else
#   bloco _False_

# exemplo de condição estruturada (maioria dos casos)
# tempo = int(input('Quantos anos tem seu carro?'))
# if tempo <=´3:
#   print('Carro novo')
# else:
#   print('Carro velho')
# print('--FIM--')

# Os comando são executados de acordo com a indentação utilizada

# Exemplo de condição simplicada
# tempo = int(input('Quantos anos tem seu carro?'))
# print('Carro novo' if tempo <=3 else'Carro velho')
# print('--FIM--')


# -------------- PRATICA -------------

# -------------- exemplo 1 -------------
nome = str(input('Qual é o seu nome? '))
if nome == 'Rafael':
    print('Nome lindo da bixiga, macho!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}!'.format(nome))


# -------------- exemplo 2 -------------

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Parabéns, você passou!')
else:
    print('Você não atingiu a média, tente novamente.')