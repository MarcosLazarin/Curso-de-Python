# Fazer um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se quer continuar.
# No final, mostre:
# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$100,00 reais.
# Qual é o nome do produto mais barato.

totalgasto = maiorque100 = ma = me = c = 0
while True:
    nomeproduto = input('Qual é o nome do produto: ')
    precoproduto = float(input('Qual é o preço: '))
    continuar = input('Você quer continuar? [S/N] ').upper().strip()
    c += 1
    totalgasto += precoproduto
    if continuar == 'N':
        break
    if precoproduto > 100:
        maiorque100 += 1
    if c == 1:
        ma = me = precoproduto = nomeproduto
    else:
        if ma > me:
            ma = precoproduto = nomeproduto
        if me < ma:
            me = precoproduto = nomeproduto
print(f'o total gasto na compra foi {totalgasto} reais.')
print(f'{maiorque100} produtos custam mais de R$100,00 reais.')
print(f'O nome do produto mais caro é {nomeproduto}.')