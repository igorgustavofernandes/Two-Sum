
num = int(input('Digite um valor inteiro: '))
tot=0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} é divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Portanto, {}} é número primo'.format(num))
else:
    print('Por ser divísivel por mais que duas vezes, {} não é número primo'.format(num))
