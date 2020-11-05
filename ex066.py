# Criar programa que leia vários números inteiros e pare quando o número 999 for digitado.
# Mostre a soma e o número de termos, desconsiderando o flag.

c = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c = c + 1
    s = s + n
print(f'A soma dos {c} termos é igual a {s}.')