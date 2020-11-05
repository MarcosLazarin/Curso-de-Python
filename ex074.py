# Criar um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# Depois, mostre a listagem de números gerados e também indique o menor e o maior valor que está na tupla

from random import randint
numeros = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
for a in numeros:
    print(f'{a} ', end='')
print(f'\nMaior número: {max(numeros)}')
print(f'Menor número: {min(numeros)}')
