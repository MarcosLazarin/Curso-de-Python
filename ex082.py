# Criar um programa que leia vários números e coloque-os em uma lista
# Depois, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente
# No final mostre os 3 conteúdos das listas.

lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Quer continuar adicionando números? [S/N] ').upper().strip()
    if continuar == 'N':
        break
for pos, valor in enumerate(lista):
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
print(f'Lista: {lista}')
print(f'Lista par: {listapar}')
print(f'Lista ímpar: {listaimpar}')