# Criar uma tupla que tenha varias palavras (não usar acentos)
# Depois deve-se mostrar, para cada palavra, quais são as suas vogais.

tupla = ('Lago', 'Azul', 'Caderno', 'Risoto', 'Aquarela', 'Piscina', 'Vogal', 'Consoante')

for a in tupla:
    print(f'\nNa palavra {a.upper()} temos as vogais: ', end='')
    for letra in a:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')