# Criar um programa que leia vários números e coloque-os em uma lista, depois disso mostre:
# Quantos números foram digitados
# A lista de valores, ordenada de foorma decrescente
# Se o valor 5 foi digitado e está ou não na lista
lista = []
while True:
    lista.append(input('Digite um número: '))
    continuar = input('Quer continuar? [S/N]').upper().strip()
    if continuar == 'N':
        break
if '5' not in lista:
    print('O valor 5 não está na lista.')
else:
    print('O valor 5 está na lista.')
print(f'Os elemento da lista são: {lista}')
lista.sort(reverse=True)
print(f'A lista em forma decrescente: {lista}')
print(f'Foram digitados um total de {len(lista)} números.')
