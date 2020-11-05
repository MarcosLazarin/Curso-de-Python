# Fazer programa que jogue par ou ímpar com o computador.
# O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
print('=' * 40)
print('{:^40}'.format('JOGO PAR OU ÍMPAR'))
print('=' * 40)
c = 0
while True:
    lista = ['P', 'I']
    e = random.choice(lista)
    n = (input('Escolha uma alternativa: [P/I] ')).upper().strip()
    print('-' * 40)
    if e == n:
        c = c + 1
    if e != n:
        break
if c == 1:
    print('Você teve 1 vitória consecutiva.')
    print('=' * 40)
    print('{:^40}'.format('GAME OVER'))
    print('=' * 40)
elif c == 0:
    print('Que pena, você não venceu nenhuma vez.')
    print('=' * 40)
    print('{:^40}'.format('GAME OVER'))
    print('=' * 40)
else:
    print(f'Você teve {c} vitórias consecutivas.')
    print('=' * 40)
    print('{:^40}'.format('GAME OVER'))
    print('=' * 40)