#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex.: Digite um número: 1834.
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
num = str(input('Digite um número de 0 a 9999: ')).strip()
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Centena: {}'.format(num[0]))