#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
frase = str(input('DIGITE UMA FRASE: ')).strip().upper()

## QUANTAS VEZES APARECE A LETRA "A".
print('A letra "A" aparece em sua frase {}'.format(frase.count('A')))

## EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
print('A posição da primeira letra "A" é o {}º caractere'.format(frase.find('A')+1))

## EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ
print('A posição da primeira letra "A" é o {}º caractere'.format(frase.rfind('A')+1))

