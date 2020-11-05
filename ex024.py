#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
cidade = str(input('Digite o nome de uma cidade: ')).strip()
n = cidade.upper().split()
print('SANTO' in n[0])

#Pode ser resolvido assim também:
cidade = str(input('Digite a cidade:')).strip()
print(cidade[:5].upper() == 'SANTO')