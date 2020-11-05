#Desenvolver um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
p = int(input('Digite aqui o 1° termo da P.A.: '))
r = int(input('Digite qual é a razão da P.A.: '))
d = p + (10 - 1) * r
for l in range(p, d + r, r):
    print('{}'.format(l), end=' -> ')
print('FIM')