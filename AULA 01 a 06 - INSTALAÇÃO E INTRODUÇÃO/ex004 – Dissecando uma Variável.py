# Aula 6 - Tipos primitivos
## Useis 'is' para saber se é possível converter o valor pelo 'is' escolhido para o formato(é número? 'isnumeric', etc)

### n = (input('Digite algo: '))
### print(n.isnumeric())

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações

n = input('Digite algo: ')
print('É sómente um espaço?', n.isspace())
print('É alfabético?', n.isalpha())
print('É alfanumérico?',n.isalnum())
print('Está em minúsculo?' ,n.islower())
print('Está em maiúsculo?', n.isupper())
print('É um número?', n.isnumeric())
print('Está capitalizada?', n.istitle())
print('O tipo primitivo desse valor é ',type(n))
