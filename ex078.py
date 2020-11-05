# Fazer programa que leia 5 valores e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor em sua respectivas posições na lista.

maior = menor = 0
lista = []
for valor in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    if valor == 0:
        maior = menor = lista[valor]
    else:
        if lista[valor] > maior:
            maior = lista[valor]
        if lista[valor] < menor:
            menor = lista[valor]
print(f'Os valores digitados foram {lista}')
print()
print(f'O maior número é o {maior}, nas posições: ', end=' ')
for pos, elem in enumerate(lista):
    if elem == maior:
        print(f'{pos}...', end=' ')
print()
print(f'\nO menor número é o {menor}, nas posições: ', end=' ')
for pos, elem in enumerate(lista):
    if elem == menor:
        print(f'{pos}...', end=' ')