lista = list()
dados = {}
mulheres = list()
maiores = list()
somaidade = media = 0
while True:
    dados["nome"] = str(input('Nome: '))
    dados["sexo"] = str(input('Sexo? [M/F]: '))
    dados["idade"] = int(input('Idade: '))
    somaidade += dados["idade"]
    lista.append(dados.copy())
    pergunta = str(input('Quer continuar? [S/N] : '))
    if dados["sexo"] in "Ff":
        mulheres.append(dados.copy())
    if dados["idade"] >= 18:
        maiores.append(dados.copy())
    if pergunta in 'Nn':
        break
media = somaidade/len(lista)
print(f'A média de idade do grupo é de {media} anos.')
print(f' As mulheres do grupo são: ', end='')
for m in mulheres:
    print(f'[{m["nome"]}]', end=' ')
print()
print(f'Os maiores de idade do grupo são: ', end='')
for d in maiores:
    print(f'[{d["nome"]}]', end=' ')
print()