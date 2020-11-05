#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
n = str(input('Digite o seu nome: ')).upper().strip()
s = n.split()
print('SILVA' in s)