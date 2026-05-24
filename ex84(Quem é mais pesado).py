pessoal = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len (pessoal)==0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoal.append(dados[:])
    dados.clear()
    pergunta = str(input('Deseja continuar? [S/N]: '))
    if pergunta in 'Nn':
        break
print(f'Você cadastrou {len(pessoal)} pessoas.')
print(f'O maior peso foi de {maior}KG. Peso de', end=' ')
for p in pessoal:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de', end=' ')
for p in pessoal:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()