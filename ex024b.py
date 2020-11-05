#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
c = str(input('Digite o nome de uma cidadela: ')).upper().strip()
cidade = c.split()
print('SANTO' in cidade[0])
print(cidade)