# Fazer um programa que simule um caixa eletrônico.
# No início pergunte ao usuário qual valor a ser sacado.
# E o programa irá dizer quantas cédulas de cada valor serão entregues.
# Obs.: Deve-se levar em consideração que o caixa possui cédulas de R$50, 20, 10 e 1 reais.

print('=' * 40)
print('{:^40}'.format('CAIXA ELETRÔNICO'))
print('=' * 40)

cedula = 50
totalcedulas = 0
valor = int(input('Qual o valor a ser sacado: R$ '))
while True:
    if valor >= cedula:
        valor -= cedula
        totalcedulas += 1
    else:
        print(f'Total de {totalcedulas} cédulas de R${cedula} reais.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedulas = 0
        if valor == 0:
            break
