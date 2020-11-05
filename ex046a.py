#Faça um programa que leia a contagem regressiva para a queima de fogos. De 10 a 0.

from time import sleep
n = int(input('Digite um número para começarmos a contagem a partir dele: '))
for c in range(n, -1, -1):
    print(c)
    sleep(0.2)
print('Buuuuuuumm!!!!')