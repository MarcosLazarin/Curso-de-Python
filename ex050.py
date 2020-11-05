#Desenvolver programa que escreva seis números inteiros e mostre a soma apenas dos números pares.
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma += + n
        cont += + 1
print('A quantidade de termos PARES é igual a: {}\nA soma desses termos PARES é igual a: {}'.format(cont, soma))