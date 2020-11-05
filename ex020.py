#O professor quer sortear a ordem de apresentação dos trabalhos dos alunos.
#Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.
import random
n1 = str(input('1°aluno: '))
n2 = str(input('2°aluno: '))
n3 = str(input('3°aluno: '))
n4 = str(input('4°aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)