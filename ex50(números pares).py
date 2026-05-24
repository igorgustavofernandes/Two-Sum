s=0
cont=0
for c in range(1, 7):
    valor = int(input('Digite o {}º valor: '.format(c)))
    if valor % 2 == 0:
        s += valor
        cont += 1
print('Você digitou {} números pares, a soma deles é = {}'.format(cont, s))
