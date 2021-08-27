# Gerenciador de Pagamentos

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal
# – 3x ou mais no cartão: 20% de juros


print('{:=^40}'.format(' BEM VINDO '))


# -- Coletando o preço
preco = float(input('Digite o valor das compras: R$'))
pagamento = int(input('''Escolha uma opção para pagamento:
[ 1 ] - Á vista em espécie 10% de desconto
[ 2 ] - Á vista no cartão: 5% de desconto
[ 3 ] - Em até 2x no cartão: preço normal
[ 4 ] - Em 3x ou mais no cartão: 20% de juros
->'''))

# -- Condições de descontos
if pagamento == 1:
    dinheiro = preco - (preco * 0.1)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no pagamento à vista em espécie.'.format(preco, dinheiro))
elif pagamento == 2:
    cartao = preco - (preco * .005)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no pagamento à vista no cartão.'.format(preco, cartao))
elif pagamento == 3:
    cartao2x = preco
    parcelamento = cartao2x / 2
    print('Sua compra de R${:.2f} vai custar R${:.2f} no pagamento em 2x no cartão.\nO valor de cada parcela será R${:.2f}'.format(preco, cartao2x, parcelamento))
elif pagamento == 4:
    parcela = int(input('Digite a quantidade de parcelas: '))
    cartao3x = preco + (preco * .2)
    parcelamento = cartao3x / parcela
    print('Sua compra de R${:.2f} vai custar R${:.2f} no pagamento em {}x no cartão.\nO valor de cada parcela será R${:.2f}'.format(preco, cartao3x, parcela, parcelamento))
else:
    print('Digite uma opção válida para pagamento.')