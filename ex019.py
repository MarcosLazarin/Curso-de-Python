# Faça um programa que ajude um professor a sortear 1 de seus 4 alunos para apagar o quadro. lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = str(input('1°aluno: '))
n2 = str(input('2°aluno: '))
n3 = str(input('3°aluno: '))
n4 = str(input('4°aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi o {}'.format(escolhido))
