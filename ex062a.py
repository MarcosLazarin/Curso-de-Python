# Fazer um programa que melhore o exercício 061.
# Mostrando ao usuário se ele quer mostrar mais alguns termos, terminando quando digitar 0.

n1 = int(input('Qual é o primeiro termo: '))
r = int(input('Qual é a razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} => '.format(n1), end='')
        n1 += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos temos você quer mostrar mais? '))
print('No total foram mostrados {} termos.'.format(total))
print('Fim')