# Faça um programa que leia o SEXO de uma pessoa, mas só aciete valores 'M' ou 'F'.
# Caso esteja errado, peça novamente até ter o valor correto

# -- Coletando dados
sexo = str(input('''Informe seu sexo: [M/F] ''')).strip().upper()[0] #com tratamento para espaços, maiúsculo e primeira letra do nome escrito

# -- Estrutura de repetição para validação
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor digíte um sexo válido: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com suceso!')

