# Escreva um programa que faça o computador jogar Jokenpô.

import random
from time import sleep
#VARIÁVEIS

n1 = 'PAPEL'
n2 = 'PEDRA'
n3 = 'TESOURA'

lista1 = [n1, n2, n3]
lista2 = [n1, n2, n3]
escolhido1 = random.choice(lista1)
escolhido2 = random.choice(lista2)

#APRESENTAÇÃO

str(input('Digite qualquer coisa para começar o programa: '))
a = str(input('Oi, tem alguém ai? Sim ou Não? ')).upper().strip()
if a == 'SIM':
    print('Ah, que legal!')
    print('Vou me apresentar, ok. Meu nome é Android 17.')
    b = str(input('Qual é o seu nome? ')).title().strip()
    print('Prazer em te conhecer, {}!'.format(b))
    print('Fui desenvolvido para jogar JOKENPO com você. Legal né!')
    c = str(input('Vamos começar? Sim ou Não? ')).upper().strip()
    if c == 'SIM':
        print('OK, legal!')
        t = str(input('Escolha uma opção: PEDRA, PAPEL ou TESOURA: ')).upper().strip()
        print('JO')
        sleep(2)
        print('KEN')
        sleep(2)
        print('PO!!')
        sleep(1)
        if escolhido1 == n1 and t == 'TESOURA':
            print('Você venceu! Eu escolhi PAPEL e você TESOURA! ')
            print('TESOURA ganha de PAPEL!')
        elif escolhido1 == n1 and t == 'PEDRA':
            print('Eu venci! Você perdeu! Eu escolhi PAPEL e você PEDRA!')
            print('PAPEL ganha de PEDRA!')
        elif escolhido1 == n1 and t == 'PAPEL':
            print('Eu não ganhei e você também não!! Ambos escolhemos PAPEL!')
        elif escolhido1 == n2 and t == 'TESOURA':
            print('Eu venci! Você perdeu! Eu escolhi PEDRA e você TESOURA!')
            print('PEDRA ganha de TESOURA!')
        elif escolhido1 == n2 and t == 'PAPEL':
            print('Você venceu! Eu escolhi PEDRA e você PAPEL!')
            print('PAPEL ganha de PEDRA!')
        elif escolhido1 == n2 and t == 'PEDRA':
            print('Eu não ganhei e você também não!! Ambos escolhemos PEDRA!')
        elif escolhido1 == n3 and t == 'TESOURA':
            print('Eu não ganhei e você também não!! Ambos escolhemos TESOURA!')
        elif escolhido1 == n3 and t == 'PAPEL':
            print('Eu venci! Você perdeu! Eu escolhi TESOURA e você PAPEL!')
            print('TESOURA ganha de PAPEL!')
        elif escolhido1 == n3 and t == 'PEDRA':
            print('Você venceu! Eu escolhi TESOURA e você PEDRA!')
            print('PEDRA ganha de TESOURA!')
    else:
        print('OK, programa encerrado!')
else:
    print('Ah, pensei que fosse alguém.')
    print('PROGRAMA ENCERRADO!')