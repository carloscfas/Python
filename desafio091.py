from random import randint
from time import sleep

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)

"""
jogos1 = {}
c = 1

for cont in range(1, 5):
    jogada = randint(1, 6)
    jogos1["jogador" + str(cont)] = jogada
print('Valores sorteados:')
for k, v in jogos1.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-=' * 30)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
jogos2 = dict(sorted(jogos1.items(), key=lambda item: item[1], reverse=True))
for k, v in jogos2.items():
    print(f'{c}o. lugar: {k} com {v}.')
    c +=1
    sleep(1)
"""
