# Desenvolver um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Qual é o 1° termo da P.A.: '))
r = int(input('Qual é a razão da P.A.: '))
u = n1 + (10 - 1) * r

for a in range(n1, u, r):
    print('{}'.format(a), end=' => ')
print('FIM')