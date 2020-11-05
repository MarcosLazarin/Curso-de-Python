#Apresentação

import random

str(input('Digite qualquer coisa para começar o programa: '))
a = str(input('Oi, tem alguém ai? Sim ou Não? ')).upper().strip()
if a == 'SIM':
    print('Ah, que legal!')
else:
    print('Ah, pensei que fosse alguém.')
    print('Progama encerrado.')
print('Vou me apresentar, ok. Meu nome é Android 17.')
b = str(input('Qual é o seu nome? ')).title().strip()
print('Prazer em te conhecer, {}!'.format(b))
print('Fui desenvolvido para jogar o jogo da adivinhação com você. Legal né!')

#Começo do jogo 1

c = str(input('Vamos começar? Sim ou Não? ')).upper().strip()
if c == 'SIM':
    print('OK, legal!')
else:
    print('OK, programa encerrado!')
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista1 = [n1, n2, n3, n4, n5]
lista2 = [n1, n2, n3, n4, n5]
lista3 = [n1, n2, n3, n4, n5]
escolhido1 = random.choice(lista1)
escolhido2 = random.choice(lista2)
escolhido3 = random.choice(lista3)
print('Preste atenção! Eu acabei de pensar em um número de 1 a 5 e você vai tentar adivinhar!')
e = int(input('Tente adivinhar o número: '))
if e == escolhido1:
    print('É isso mesmo, você acertou!!!')
    print('Eu escolhi o {}, você é muito bom nesse jogo!'.format(escolhido1))
else:
    print('Você errou, que pena!')
    print('O número que eu escolhi foi o {}, quem sabe na próxima!'.format(escolhido1))

#Começo do jogo 2

d = str(input('Quer jogar novamente? Sim ou Não? ')).upper().strip()
if d == 'SIM':
    print('Ok, vamos lá!')
    f = int(input('Tente adivinhar o número: '))
    if f == escolhido2:
        print('Você acertou! Parabéns!!')
        print('Eu escolhi o número {} e você adivinhou. Parabéns!'.format(escolhido2))
    else:
        print('Você errou, que pena!')
        print('O número que eu escolhi desta vez foi o {}, não desista e tente novamente!'.format(escolhido2))
else:
    print('OK, programa encerrado!')

#Começo do jogo 3

g = str(input('Que tentar acertar uma última vez? Sim ou Não?')).upper().strip()
if g == 'SIM':
    print('Ok, vai ser a última vez!')
    h = int(input('Tente adivinhar o número: '))
    if h == escolhido3:
        print('Acertooou! Parabéns {}!'.format(b))
        print('Desta vez eu escolhi o {} e você acertou. TOP DE MAIS'.format(escolhido3))
    else:
        print('Você errou!!')
        print('O número que eu escolhi desta vez foi o {}.!'.format(escolhido3))
        print('Obrigado por jogar! Espero te ver aqui outras vezes. Até maaaissss!!')
else:
    print('OK, programa encerrado!')

print('___FIM___DE___JOGO___')