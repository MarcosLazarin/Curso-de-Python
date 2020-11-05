# Refazer o exercício 35 dos triângulos.
# Mostarndo desta vez se o triângulo é:
# 1) Equilátero: Todos os lados iguais
# 2) Isósceles: Dois lados iguais
# 3) Escaleno: Todos os lados diferentes

print('=-=' * 20)
print('ANALISADOR DE TEXTO')
print('=-=' * 20)
r1 = float(input('Digite o 1° valor: '))
r2 = float(input('Digite o 2° valor: '))
r3 = float(input('Digite o 3° valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores podem formar um triângulo.')
    if r1 == r2 == r3:
        print('Este triângulo é equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Este triângulo é escaleno.')
    else:
        print('Este triângulo é isósceles.')
else:
    print('Os valores não podem formar um triângulo.')
print('=-=' * 20)
print('ANALISADOR DE TEXTO')
print('=-=' * 20)