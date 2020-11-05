#Faça um programa que leia a contagem regressiva para a queima de fogos. De 10 a 0.
#Colocar um emoji

from time import sleep

print('A contagem regressiva para a queima de fogos irá começar!')
sleep(2)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fogos!!!!')
