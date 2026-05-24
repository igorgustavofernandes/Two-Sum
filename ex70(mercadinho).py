total = 0
maisdecem = 0
pichincha = ''
menorpreco = 0
contador = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: R$'))
    contador += 1
    if valor > 100:
        maisdecem += 1
    total += valor
    if contador == 1 or valor < menorpreco:
        menorpreco = valor
        pichincha = nome
    escolha = str(input('Quer continuar? [S/N] : ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'O valor total da sua compra é de R$ {total}')
print(f'Na sua compra {maisdecem} produtos custam mais de R$100')
print(f'O produto mais barato é a {pichincha}')
