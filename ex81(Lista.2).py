lista = list()
while True:
    num = int(input('Digite um número para a lista: '))
    lista.append(num)
    desejo = str(input('Quer continuar? [S/N] ')).strip().upper()
    if desejo == 'N':
        break
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Do maior para o menor fica{lista}')
if 5 not in lista:
    print('Não tem cinco na lista')
else:
    print('Tem cinco na lista')