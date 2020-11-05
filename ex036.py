# Escreva um  programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador, e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa a ser financiada? R$'))
salario = float(input('Qual é o seu salário atual? R$'))
tempo = int(input('Em quantos anos você pretende pagar o empréstimo? '))
parcelas = casa/(tempo * 12)
print('Lembre-se, para o empréstimo ser aprovado em nosso banco as parcelas não podem ser <= 30% de seu salário')
if parcelas <= salario * 0.3:
    print('Seu financiamento foi aprovado! Parabéns!!!')
    print('A sua prestação mensal é de {}, e você irá pagar em {} meses.'.format(parcelas, tempo * 12))
else:
    print('Infelizmente seu empréstimo foi negado, pois as parcelas passam o valor de 30% do seu salário.')