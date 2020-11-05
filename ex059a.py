#Fazer um programa que leia dois números e mostre um menú na tela:
#[1] Somar
#[2] Múltiplicar
#[3] Maior
#[4] Novos números
#[5] Sair do programa
# O programa deve realiar a solicitação feita em cada opção em loop.

print('<>' * 20)
n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n = 0
while n != 5:
    print('Escolha uma das opções para prosseguir:')
    print("""[1] Somar os números\n[2] Múltiplicar os números\n[3] Mostrar qual é maior número\n[4] Digitar novos números\n[5] Sair do programa""")
    n = int(input('Opção: '))
    if n == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif n == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif n == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        elif n1 < n2:
            print('O maior número é {}.'.format(n2))
    elif n == 4:
        print('Insira os novos números: ')
        n1 = float(input('Digite o 1° número: '))
        n2 = float(input('Digite o 2° número: '))
    else:
        print('Fim do programa!')
print('PROGRAMA ENCERRADO!')
print('<>' * 20)