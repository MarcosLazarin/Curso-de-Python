# Escreva um programa que leia dois números e mostre uma mensagem na tela:
# - O primeiro valor é maior
# - o segundo valor é maior
# - Não exxiste valor maior, os dois são iguais

n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
if n1 > n2:
    print('{} é maior que {}.'.format(n1, n2))
elif n1 < n2:
    print('{} é maior que {}.'.format(n2, n1))
else:
    print('{} é igual a {}.'.format(n1, n2))
