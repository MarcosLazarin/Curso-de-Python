#Escreva um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex.: Ana Maria de Souza
#primeiro = Ana
#último = Souza
nome = str(input('Digite seu nome: ')).strip()
s = nome.split()
print('Seu primeiro nome é {}'.format(s[0]))
#print('Seu último nome é {}'.format(s[len(s)-1]))
print('Seu último nome é {}'.format(s[-1]))
