#Escrever um programa que identifique se a palavra é ou não um palíndromo.
#ex.: APOS A SOPA. A SACADA DA CASA. A TORRE DA DERROTA. O LOBO AMA O BOLO. ANOTARAM A DATA DA MARATONA.
frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")