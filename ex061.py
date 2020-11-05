#Fazer um programa refazendo o exercício 051, mostrando os 10 primeiros termos progressão usando a estrutura while.

n1 = int(input('Qual é o primeiro termo: '))
r = int(input('Qual é a razão: '))
c = 1
while c <= 10:
    print('{} ---> '.format(n1), end=' ')
    n1 += r
    c += 1
print('FIM')
