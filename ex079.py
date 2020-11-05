# Criar um programa onde o usuário possa digitar vários valores e cadastre-os em uma lista
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescentes.

lista = []
while True:
    p = (int(input('Digite um número para adicionar na lista: ')))
    if p not in lista:
        lista.append(p)
    else:
        print('Valor duplicado')
    r = input('Quer continuar? [S/N]').upper().strip()
    if r == 'N':
        break
lista.sort()
print(lista)
