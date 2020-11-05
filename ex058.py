#Fazer um programa que melhore o desafio 028.
#Só que agora o jogador vai jogar até advinhar o número.
#Mostrando no final quantos palpites foram necessários.

#Apresentação do jogo

import random

#Começo do jogo 1
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista1 = [n1, n2, n3, n4, n5]
escolhido1 = random.choice(lista1)
c = str(input('Vamos começar? Sim ou Não? ')).upper().strip()
if c == 'SIM':
    print('OK, legal!')
    acertou = False
    palpite = 0
    print('Preste atenção! Eu acabei de pensar em um número de 1 a 5 e você vai tentar adivinhar!')
    while not acertou:
        e = int(input('Tente adivinhar o número: '))
        palpite += 1
        if e == escolhido1:
            acertou = True
            print('É isso mesmo, você acertou!!!')
            print('Eu escolhi o {}, você é muito bom nesse jogo!'.format(escolhido1))
        else:
            print('Você errou, que pena!')
            print('O número que eu escolhi foi o {}, quem sabe na próxima!'.format(escolhido1))
    print('Você precisou de {} palpites para acertar!'.format(palpite))
else:
    print('OK, programa encerrado!')
print('___FIM___DE___JOGO___')