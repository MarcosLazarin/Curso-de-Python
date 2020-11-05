#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite um ângulo: '))
s = math.sin(math.radians(a))
print('Seno: {:.2f}'.format(s))
c = math.cos(math.radians(a))
print('Cosseno: {:.2f}'.format(c))
t = math.tan(math.radians(a))
print('Tangente: {:.2f}'.format(t))