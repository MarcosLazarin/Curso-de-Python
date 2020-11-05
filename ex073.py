# Criar uma tupla preenchida com os 20 primeiros colocados do Brasileirão, depois mostrar.
# Apenas os 5 primeiros colocados
# Os últimos 4 colocados na tabela
# Os times em ordem alfabética
# em que posição está o Internacional

tabela = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras',
          'Vasco', 'Flamengo', 'Fluminense', 'Sport', 'Santos',
          'Fortaleza', 'Athlético-PR', 'Ceará', 'Atlético-GO',
          'Grêmio', 'Corinthians', 'Coritiba', 'RB Bragantino',
          'Botafogo', 'Goiás', 'Bahia')
print('=' * 40)
print('{:^40}'.format('TABELA'))
print('=' * 40)
for times in tabela:
    print((tabela.index(times)+1), end=')')
    print(times)
print('=' * 40)
print('{:^40}'.format('4 primeiros colocados'))
print('=' * 40)
print(f"""Os 4 primeiros colocados são: 
1° {tabela[0]}
2° {tabela[1]}
3° {tabela[2]}
4° {tabela[3]}""")
print('=' * 40)
print('{:^40}'.format('4 últimos colocados'))
print('=' * 40)
print(f"""Os 4 últimos colocados são:
17° {tabela[16]}
18° {tabela[17]}
19° {tabela[18]}
20° {tabela[19]}""")
print('=' * 40)
print('{:^40}'.format('Times em ordem alfabética'))
print('=' * 40)
for t in sorted(tabela):
    print(t)
print('=' * 40)
print('{:^40}'.format('Posição do Internacional'))
print('=' * 40)
print(tabela.index('Internacional')+1)
