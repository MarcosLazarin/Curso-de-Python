#Escreva um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex.: Ana Maria de Souza
#primeiro = Ana
#último = Souza
n = str(input('Digite seu nome: '))
nome = n.split()
print('Seu primerio nome é {} \nSeu último nome é {}'.format(nome[0], nome[-1]))