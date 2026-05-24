ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-'*30)
print(f'{"Nº":<4}{"Nome":<10}{"Media":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    resp = int(input('Quer mostrar as notas de qual aluno? [999 PARA] '))
    if resp == 999:
        print('Finalizando...')
        break
    if resp <= len(ficha) - 1:
       print(f'Notas de {ficha[resp][0]} e {ficha[resp][1]}')
print('Volte sempre!')