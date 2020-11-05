#Fazer um programa que leia um número inteiro e diga se ele é ou não número primo.
#Lembrando que um número primo é considerado assim por ser divisível por 1 e por ele mesmo.

c = 0
n = int(input('Digite um número para saber se ele é primo: '))
for l in range(1, n + 1):
    if n % l == 0:
        c+= 1
if c == 2:
    print('Este número é primo!')
else:
    print('Este número não é primo!')