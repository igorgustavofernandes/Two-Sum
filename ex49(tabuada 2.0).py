print('-='*20)
print('TABUADA')
print('-='*20)
v = int(input('Digite o valor qual você deseja descobrir a tabuada: '))
for c in range (0, 10+1):
    print('{} x {} = {}'.format(v, c, v*c))
