#Fazer um programa que leia um número inteiro e diga se ele é ou não número primo.
#Lembrando que um número primo é considerado assim por ser divisível por 1 e por ele mesmo.
n = int(input('Digite um número para saber se ele é primo: '))
cont = 0
for a in range(1, n + 1):
    if n % a == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(a), end='')
print('\nO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('Este número é primo')
else:
    print('Este número não é primo')

