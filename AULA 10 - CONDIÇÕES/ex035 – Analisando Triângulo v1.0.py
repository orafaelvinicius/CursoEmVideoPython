# Desenvolda um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('=-'*20)
print('Analisador de triângulos')
print('=-'*20)
r1 = float(input('Qual o primeiro seguimento? '))
r2 = float(input('Qual o segundo seguimento? '))
r3 = float(input('Qual o terceiro seguimento? '))

#-- Verificando os seguimentos
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo')
else:
    print('Os seguimentos acima NÃO podem formar um triângulo')

