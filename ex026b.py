#Crie um programa que leia uma frase pelo teclado e mostre.
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez
f = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes.'.format(f.count('A')))
print('A primeira letra "A" aparece na posição {}.'.format(f.find('A')))
print('A última vez que a letra "A" aparece é na posição {}.'.format(f.rfind('A')))
