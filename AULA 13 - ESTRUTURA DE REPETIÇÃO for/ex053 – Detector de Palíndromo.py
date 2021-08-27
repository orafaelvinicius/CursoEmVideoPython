# Crie um programa que leia uma FRASE qualquer e diga se ela é um PALINDROMO, desconsiderando os espaços (e acentos também)
# Palindromo são palavras que lendo de trás pra frente não são alteradas.
''' ex: APOS A SOPA,
A SACADA DA CASA,
A TORRE DA DERROTA,
O LOBO AMA BOLO,
ANOTARAM A DATA DA MARATONA'''

# -- Lendo a frase
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
# MACETE DE FATIAMENTO: Você também pode usar a variável "inverso = junto[::-1]" para ler o nome de trás pra frente.

# -- Laço e condições para descobrir o palindromo
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase {} escrita em ordem inversa fica {}.'.format(junto, inverso))
if inverso == junto:
    print('Esta frase É UM PALINDROMO!')
else:
    print('Esta frase NÃO É UM PALINDROMO.')
