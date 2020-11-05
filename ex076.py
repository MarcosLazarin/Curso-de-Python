# Criar uma tupla única com nomes de produtos e seus respectivos preços, na sequência
# No final, mostre uma listagem de preços, organizando os dados em forma tabular

tupla = ('Lápis', 1.99, 'Caneta', 1.00, 'Lapizeira', 3.99, 'Caderno', 12.99, 'Régua', 2.98, 'Borracha', 0.30)

for p in range (len(tupla)):
    if p % 2 == 0:
        print(f'{tupla[p]:.<30}', end=' ')
    else:
        print(f'R${tupla[p]:>7.2f}')