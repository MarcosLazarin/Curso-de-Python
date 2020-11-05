#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
import math
c1 = float(input('Cateto Oposto: '))
c2 = float(input('Cateto Adjacente: '))
h = math.hypot(c1, c2)
print('O cateto oposto {} + o cateto adjacente {} resultam na hipotenusa {:.2f}.'.format(c1, c2, h))


