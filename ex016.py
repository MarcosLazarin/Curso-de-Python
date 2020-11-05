#Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.
from math import trunc
n = float(input('Digite um número: '))
print('A porção inteira de {} é igua a {}.'.format(n, trunc(n)))
n2 = float(input('Digite outro número: '))
print('A porção inteira de {} é igual a {}'.format(n2, trunc(n2)))
