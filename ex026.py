#Crie um programa que leia uma frase pelo teclado e mostre.
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez
frase = str(input('Digite uma frase: ')).strip().upper()
print('Esta frase tem {} letras "a". '.format(frase.count('A')+1))
print('A primeira vez que a letra "a" aparece é na posição {}.'.format(frase.find('A')))
print('A última vez em que a letra "a" aparece é na posição {}.'.format(frase.rfind('A')))