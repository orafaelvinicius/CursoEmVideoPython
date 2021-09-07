'''
Crie um programa que leia DOIS VALRORES e mostre um MENU na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novo número
    [5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('''Escolha uma das opções:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novo número
        [5] sair do programa
    ''')
    opcao = int(input('>>>>Digite uma das opções: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'\033[1;34;40mA soma entre {n1} + {n2} é igual a \033[1;33;40m{soma}.\33[m')

    elif opcao == 2:
        multi = n1 * n2
        print(f'\033[1;34;40mA multiplicação entre {n1} x {n2} é igual a \033[1;33;40m{multi}.\033[m')

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'\033[1;34;40mEntre {n1} e {n2} o \033[1;33;40m{maior}\033[1;34;40m é o maior.\033[m')

    elif opcao == 4:
        print('Informe os valores novamente.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
print('Obrigado por utilizar minha calculadora. Tchau!')

