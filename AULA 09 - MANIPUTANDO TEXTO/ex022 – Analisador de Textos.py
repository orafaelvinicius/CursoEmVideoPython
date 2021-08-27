# CRIE UM PROGRAMA QUE LEIA NO NOME COMPLETO DE UMA PESSOA Q MOSTRE:

nome = str(input('DIGITE O SEU NOME COMPLETO: ')).strip()
print('Analisando seu nome...')

    ## O NOME COM TODAS AS LETRAS MAIÚSCULAS
print(('Seu nome com todas as letras maipusculas é: {}.'.format(nome.upper())))

    ## O NOME COM TODAS AS LETRAS MINÚSCULAS
print(('Seu nome com todas as letras minúsculas é: {}.'.format(nome.lower())))

    ## QUANTAS LETRAS AO T0DO (SEM CONTAR ESPAÇO)
print(('Seu nome tem {} letras.'.format(len(nome)-nome.count(' '))))

    ## QUANTAS LETRAS TEM O PRIMEIRO NOME
separado = nome.split()
print('Seu primeiro é {} e ele tem {} letras'.format(separado[0], len(separado[0]))) #cód da primeira tentativa

#JEITO 2 - print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
