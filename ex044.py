# Escreva um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# 1) À vista Dinheiro/Cheque = 10% de desconto
# 2) À vista no cartão = 5% de desconto
# 3) Em até 2x no cartão = Preço normal
# 4) Em 3x ou mais = 20% de juros.

compra = float(input('Qual é o valor das suas compras? R$'))
print("""Escolha uma das formas de pagamento:
 (1) À vista Dinheiro
 (2) À vista Cartão
 (3) Cartão 2x
 (4) Cartão 3x ou mais """)
pagamento = int(input('Escolha a forma de pagamento: '))
if pagamento == 1:
    print('O valor de suas compra foram R${} reais \ne você escolheu pagar à vista no dinheiro, \nrecebendo um desconto de R${} rais. \nTotal a pagar: R${} reais'.format(compra, compra * 0.1, compra * 0.9))
elif pagamento == 2:
    print('O valor de suas compras foram R${} reais \ne você escolheu pagar à vista no cartão, \nrecebendo um desconto de R${} reais. \nTotal a pagar: R${} reais'.format(compra, compra * 0.05, compra * 0.95))
elif pagamento == 3:
    print('O valor de suas compras foram R${} reais \ne você escolheu pagar em 2x no cartão, \nnão recebendo desconto. \nValor de cada parcela: R${} reais'.format(compra, compra / 2))
elif pagamento == 4:
    print('O valor de suas compras foram R${} reais \ne você escolheu pagar em 3x no cartão, \nsendo necessário ser acrescidos 20% de juros. \nValor de cada parcela: R${:.3f} reais \nTotal de juros: R${} \nTotal a pagar R${}'.format(compra, compra / 3, compra * 0.2, compra * 1.2))
else:
    print('Opção não identificada!')