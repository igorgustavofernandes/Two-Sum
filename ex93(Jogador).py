dados = dict()
dados['nome'] = str(input('Nome do "jogador caro": '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
gols = list()
for c in range(0, dados['partidas']):
    dados["gol"] = int(input(f'Quantos gols {dados["nome"]} fez na {c + 1}º partida: '))
    gols.append(dados["gol"])
dados['gols'] = gols
dados['total de gols'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas.')
for i, g in enumerate(dados['gols']):
    print(f'=> Na partida {i+1}, o jogador fez {g} gols.')
print(f'Um total de {dados["total de gols"]} gols.')