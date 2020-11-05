#Desenvolver programa que escreva seis números inteiros e mostre a soma apenas dos números pares.
c = 0
s = 0
for l in range(1, 7):
    a = int(input('Escreva o {} termo: '.format(l)))
    if a % 2 == 0:
        s = s + a
        c = c + 1
print('A quantidade de termos pares é {}, e soma deles é {}.'.format(c, s))
