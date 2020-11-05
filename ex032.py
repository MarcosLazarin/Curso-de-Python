#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
a = int(input('Digite o ano que você quer analisar: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))