#Fazer um programa que leia vários números perguntando se quer continuar.
#Deve ser mostrado a média entre eles, qual é o maior e o menor número.

a = s = c = 0
a = 'S'
ma = me = 0
while a in 'Ss':
        n = int(input('Digite um número: '))
        s += n
        c += 1
        if c == 1:
            ma = me = n
        else:
            if ma > n:
                ma = n
            if me < n:
                me = n
        a = input('Você quer continuar? [S/N]').strip().upper()
me = s/c
print(f'A média dos números é igual a {me}.')
print('Fim')
