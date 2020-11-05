#Fazer um programa que leia vários números inteiros e pare quando digitar 999.
#Mostrando no final quantos números foram digitados e a soma entre eles.
n = 0
c = 0
s = 0
n = int(input('Digite um número:'))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número:'))
print('A soma dos termos é igual a {}.'.format(s))
print('O número total de termos é igual a {}.'.format(c))