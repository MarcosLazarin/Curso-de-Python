#Fazer um programa que leia dois números e mostre um menú na tela:
#[1] Somar
#[2] Múltiplicar
#[3] Maior
#[4] Novos números
#[5] Sair do programa
# O programa deve realiar a solicitação feita em cada opção em loop.

from time import sleep

print('=-=' * 25)
print('Programa iniciando, aguarde...')
sleep(2)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n = 0
sleep(2)
while n != 5:
    print('''Escolha uma opção para proseguir
    [1] Somar
    [2] Múltiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    n = int(input('Digite a opção que você deseja: '))
    if n == 1:
        print('{} + {} = {}'.format(n1, n2, n1 * n2))
        sleep(2)
    elif n == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
        sleep(2)
    elif n == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
            sleep(2)
        else:
            print('O maior número é {}.'.format(n2))
            sleep(2)
    elif n == 4:
        print('Informe os novos valores:')
        sleep(1)
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        sleep(2)
    elif n == 5:
        print('Programa encerrado!')
        sleep(2)
print('Fim do programa!')
print('=-=' * 25)