#Criar programa que mostre todos os números pares entre 1 e 50.
n = int(input('Digite o último número para saber quais números são pares: '))
for a in range(2, n+1, 2):
    print(a)
