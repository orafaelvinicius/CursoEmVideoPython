# Índice de Massa Corporal (IMC)
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

# -- Coletando o peso e altura
peso = float(input('Qual é o seu peso atual? (Kg) '))
altura = float(input('Qual a sua altura em metros? '))

# -- Calculando IMC
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}.'.format(imc), end='')

# -- Condições
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal')
elif 18.5 <= imc < 25:
    print('Você está na faixa de peso NORMAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está OBESO')
elif imc >= 40:
    print('com obesidade MORBIDA!')
else:
    print('Desculpa, não foi possível calcular seu IMC. Tente novamente.')