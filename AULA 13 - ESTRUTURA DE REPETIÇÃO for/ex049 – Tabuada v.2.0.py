# Refaça o ex009, mostreando a TABUADA de um número que o usuário escolher, só que agora utilizando um LAÇO FOR

#-- Coletando o número
n = int(input('Digite um número para ver sua tabuada: '))
print('A tabuada de {} é:'.format(n))

#-- Laço para tabuada
for t in range(1, 11):
    print('{} x {} = {}'.format(n, t, n*t))
