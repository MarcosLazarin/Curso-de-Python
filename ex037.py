# Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão:
# 1) Binário
# 2) Octal
# 3) Hexadecimal
num = int(input('Digite um número inteiro: '))
print("""Escolha para qual base você quer converter:
[1] Binário
[2] Hexadecimal
[3] Binário""")
op = int(input('Sua opção: '))
if op == 1:
    print('O número {} em Binário é igual a: {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} em Hexadecimal é igual a: {}'.format(num, hex(num)[2:]))
elif op == 3:
    print('O número {} em Octal é igual a: {}'.format(num, oct(num)[2:]))
else:
    print('operação inválida! Tente novamente')