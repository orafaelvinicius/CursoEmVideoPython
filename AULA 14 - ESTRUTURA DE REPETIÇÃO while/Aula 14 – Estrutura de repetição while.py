# Enquanto o "for" é uma estrutura de repetição com variável de comando, o WHILE é uma estrutura de repetição com TESTE LÓGICO

# O while vai repetir o reste lógico até que ele seja FALSO

# Exemplo:
'''
Em portugol:
enquanto não maça:
    passo
pega

Em Python
while not maça:
    passa
pega
'''

# A grande vantagem do WHILE é que não existe um padrão de contiuidade
# Você pode/deve utilizar o WHILE com condições "ifs".
'''
Ex:
while not maça:     #Enquanto não houver o objeto, as condições serão utilizadas
    if tem chão?
        anda
    if tem buraco?
        pula
    if tem moeda?
        pega
pega
'''

# SE VOCÊ SABE O LIMITE DO RANGE, PODE USAR FOR OU WHILE, SE NÃO SOUBER, USE O WHILE


# -- Prática

print('Contando até 9')
contador = 1
while contador < 10:     # Enquanto o contador NÃO CHEGAR a 10
    print(c)
    contador += 1

print('Lendo vários valores (até digitar 0 como CONDIÇÃO DE PARADA "flag".')
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('parou')

print('Continuidade com 2 variváveis')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar [ S / N ]: ')).upper()
print('fim')


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:

            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
print('Programa fechado')

