#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex.: Digite um número: 1834.
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
n = str(input('Digite uma milhar: '))
print('Milhar: {} \nCentena: {} \nDezena: {} \nUnidade: {}'.format(n[0], n[1], n[2], n[3]))
