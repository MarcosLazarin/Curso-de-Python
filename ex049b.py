#Refazer o ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço FOR.

n = int(input('Digite um número que você queira saber a tabuada: '))
for a in range(1, 11):
    print('{} x {} = {}'.format(n, a, n * a))
