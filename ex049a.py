#Refazer o ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço FOR.
n = int(input('Digite um número para saber sua tabuada: '))
for l in range(0, 11):
    print('{} x {} = {}'.format(n, l, n * l))
    