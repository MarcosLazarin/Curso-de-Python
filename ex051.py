# Desenvolver um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
a = int(input('Qual é o 1° termo da sua P.A.: '))
b = int(input('Qual é a razão da P.A.: '))
d = a + (10 - 1) * b
for c in range(a, d + b, b):
    print('{}'.format(c), end=' -> ')
print('Fim')
