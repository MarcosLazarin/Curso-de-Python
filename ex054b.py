# Criar programa que leia a data de nascimento de 7 pessoas.
# No final mostre quantas pessoas são maiores de 18 e quantas não são.
from datetime import date

hoje = date.today()
ano = hoje.year
ma = 0
me = 0

for p in range(1, 8, 1):
    pessoas = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(p)))
    idade = ano - pessoas
    if idade > 18:
        ma += 1
    else:
        me += 1
print('O números de menores é igua a {} \nO números de maiores é igual a {}.'.format(me, ma))