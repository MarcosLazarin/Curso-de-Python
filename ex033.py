#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#Valor
a = float(input('Digite o 1° valor: '))
b: float = float(input('Digite o 2° valor: '))
c = float(input('Digite o 3° valor: '))
#Menor
me = a
if b < a and b < c:
    me = b
if c < a and c < b:
    me = c
#Maior
ma = a
if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c
#Resultado
print('O maior valor é {} é o menor valor é {}.'.format(ma, me))