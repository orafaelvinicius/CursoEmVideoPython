# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. Se não, mostre apenas a velocidade.
## A multa vai custar R$7,00 por cada km acima do limite.

# ---------- Velocidade
velocidade = float(input('Qual a velocidade que seu carro passou em km/h? '))
print('Seu carro passou a {:.0f}km/h.\n'.format(velocidade))

# ---------- Multa

multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('Velocidade aceitável. \nVocê não foi multado.')
else:
    print('Você foi multado por exceder o limite de velocidade!\nO valor da sua multa é de R${:.2f}'.format(multa))

print('\nTenha um bom dia. Dirija com segurança!')