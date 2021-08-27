# AULA 08 - TRABALHANDO COM MODULOS
# Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de  {} é igual a {}'.format(num, math.ceil(raiz)))

# VocÊ pode importar apenas uma parte do módulo colocando o um "from" para importartar apenas a função desejada (assim dá pra poupar memoria do programa)
    # ex: from math import sqrt, floor, etc...

