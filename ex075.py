# Fazer programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o 9
# Em que posição foi digitado o primeiro 3
# Quais foram os números pares

n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O primeiro três foi digitado na posição {n.index(3)+1}')
else:
    print(f'A tupla não contém nenhum valor 3.')
print('Os valores pares são: ', end='')
for a in n:
    if a % 2 == 0:
        print(a, end=' ')