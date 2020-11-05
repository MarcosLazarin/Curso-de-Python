#Fazer um programa que leia um número inteiro e diga se ele é ou não número primo.
#Lembrando que um número primo é considerado assim por ser divisível por 1 e por ele mesmo.

n = int(input('Digite um número para saber se ele é primo: '))
c = 0
for a in range(1, n + 1):
    if n % a == 0:
        c += 1
if c == 2:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo.'.format(n))
print('FIM')
