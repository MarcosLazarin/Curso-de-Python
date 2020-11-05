#Criar programa que leia a data de nascimento de 7 pessoas. No final mostre quantas pessoas são maiores de 18 e quantas não são.
from datetime import date
hoje = date.today()
ano = hoje.year
maiores = 0
menores = 0
for l in range(1,8):
    d = int(input('A data de nascimento da {} pessoa: '.format(l)))
    idade = ano - d
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('{} pessoas são maiores de idade. \n{} pessoas são menores de idade.'.format(maiores, menores))
