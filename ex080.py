# Criar um programa que leia cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort())
# No final mostre a lista em ordem

maior = menor = 0
lista = []
for c in range(0, 4):
    a = int(input('Digite um valor: '))
    if c == 0 or a > lista[-1]:
        lista.append(a)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if a <= lista[pos]:
                lista.insert(pos, a)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {lista}')