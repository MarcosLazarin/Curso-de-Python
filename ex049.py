#Refazer o ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço FOR.
num = int(input('Digite um número para saber sua tabuada: '))
for a in range(1, 11):
    print('{} x {} = {}'.format(num, a, num * a))