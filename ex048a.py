#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
c = 0
s = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        c += 1
        s += a
print('A soma de {} termos ímpares é igual a {}.'.format(c, s))