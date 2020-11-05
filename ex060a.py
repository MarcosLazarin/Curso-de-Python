#Fazer um programa que leia um número e mostre seu fatorial
# ex.: 5! = 5 x 4 X 3 X 2 X 1 = 120

n = int(input('Digite um número para saber o seu fatorial: '))
f = 1
while n > 0:
    print('{} '.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    f *= n
    n -= 1
print(f)