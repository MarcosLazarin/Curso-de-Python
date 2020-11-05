#Desenvolver programa que escreva seis números inteiros e mostre a soma apenas dos números pares.
c = 0
s = 0
for a in range(1, 7):
    n = int(input('Digite o {}° número: '.format(a)))
    if n % 2 == 0:
        c += 1
        s += n
print('A soma de {} números pares é igual a {}.'.format(c, s))
