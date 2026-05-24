from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
dado = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6),
        'Jogador5': randint(1, 6),
        'Jogador6': randint(1, 6)}
for k, v in dado.items():
    print(f'O {k} recebeu {v}')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('-='*10)
print('Ranking dos jogadores')
print('-='*10)
for i, v in enumerate(ranking):
        print(f'{i + 1}º {v[0]} com {v[1]}')