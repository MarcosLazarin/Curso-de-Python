#Fazer um programa que leia um número inteiro e mostre uma sequência de fibonnaci.
# ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
n = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
c = 3
print('{} -> {}'.format(n1, n2), end='')
while c <= n:
    n3 = n1 + n2
    print('-> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    c += 1
print(' -> FIM')