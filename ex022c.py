#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas as letras minúsculas.
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome.
nome = str(input('Digite aqui o seu nome: ')).strip()
print('Seu nome com letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome com letras minúscula é {}.'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
s = nome.split()
print('Seu primerio nome é {} e ele tem {} letras.'.format(s[0], len(s[0])))
