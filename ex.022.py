#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas as letras minúsculas.
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome.

    #.strip() é usado para tirar os espaços que irão haver no começo e no final da variável 'nome'.
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é: {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}.'.format(nome.lower()))
    #len(nome) irá contabilizar o número de letras - nome.count(' ') que contabiliza espaços e irá removelos da conta.
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
    #Foi criado uma variável nova para dividir em grupos a variável 'nome'.
s = nome.split()
    #s[] está dizendo que aparecerá na tela o grupo do nome 0, e len(s[0]) está dizendo que será contado as letras desse grupo.
print('O seu primeiro nome que é {}, tem {} letras.'.format(s[0], len(s[0])))