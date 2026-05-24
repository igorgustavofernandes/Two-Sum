print('-='*20)
print('Os 10 primeiros termos de uma PA')
print('-='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1

while cont <= 10:
    print(f'{termo}', end=' → ')
    termo += razao
    cont += 1

print('FIM')