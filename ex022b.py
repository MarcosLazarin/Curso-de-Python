#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas as letras minúsculas.
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome.

nome =  str(input('Qual o seu nome completo: '))
print('Seu nome completo em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}.'.format(nome.lower()))
print('Seu nome sem espaços tem {} letras.'.format(len(nome) - nome.count(' ')))
p = nome.split()
print('Seu primeiro nome tem é {} e tem {} letras.'.format(p[0], len(p[0])))