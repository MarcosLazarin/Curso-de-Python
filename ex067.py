# Fazer programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário.
# O programa será interrompido quando o usuário digitar um número negativo.

print('(:)' * 20)
print('{:^60}'.format('TABUADA'))
print('(:)' * 20)

while True:
    c = 0
    print('-' * 60)
    n = int(input('Digite um número para saber sua tabuada: '))
    print('-' * 60)
    if n < 0:
        break
    while c <=10:
        print(f'{n} x {c} = {n * c}')
        c = c + 1
print('(:)' * 20)
print('{:^60}'.format('PROGRAMA ENCERRADO'))
print('(:)' * 20)