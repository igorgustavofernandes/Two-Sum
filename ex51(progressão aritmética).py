print('-='*20)
print('Os 10 primeiros termos de uma PA')
print('-='*20)
pt = int(input('Digite o primeiro termo: '))
razao = int (input('Digite a razão: '))
decimo = pt + (10 - 1) * razao
for c in range(pt, decimo, razao):
    print(c, end='->')
print('FIM')
print('-='*30)