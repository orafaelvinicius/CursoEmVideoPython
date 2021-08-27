# Desenvolva um programa que pergunte a distância da viagem em km.
# calcule o preço da passagem cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas

# ---------- Lendo a distância da viagem
distancia = float(input('Qual a distância da sua viagem em Km? '))
print('=*'*20)
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
print('=*'*20)

# ---------- Condições
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print('O valor da sua passagem será R${:.2f}'.format(preco))
