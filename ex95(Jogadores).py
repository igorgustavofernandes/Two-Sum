jogadores = list()
dados = dict()
while True:
    gols = list()
    dados['nome'] = str(input('Nome: '))
    dados['partidas'] = int(input(f'Quantas partidas, o {dados["nome"]} jogou?: '))
    for c in range(0, dados["partidas"]):
        gols.append(int(input(f'Quantos gols {dados["nome"]} fez na {c + 1}º partida: ')))
    dados['gols'] = gols.copy()
    dados['total'] = sum(dados['gols'])
    jogadores.append(dados.copy())
    pergunta = str(input('Quer continuar? [S/N] '))
    if pergunta in 'Nn':
        break
print('-='*30)
print(f'{"Nº":<4}{"Nome":<15}{"Gols por Partida":<20}{"Total":>5}')
for i, a in enumerate(jogadores):
    print(f'{i:<4}{a["nome"]:<15}{str(a["gols"]):<20}{a["total"]:>5}')