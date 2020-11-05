#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*20)
print('ANALISADOR DE TEXTO')
print('-='*20)
r1 = float(input('Digite o 1° valor: '))
r2 = float(input('Digite o 2° valor: '))
r3 = float(input('Digite o 3° valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores podem formar um triângulo.')
else:
    print('Os valores não podem formar um triângulo.')