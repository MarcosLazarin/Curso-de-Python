#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
nome = str(input('Qual é o seu nome? ')).strip()
s = nome.upper().split()
print('SILVA' in s)

#Pode ser resolvido assim também:
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))