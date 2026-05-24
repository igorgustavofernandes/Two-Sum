from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print(f'{"MEGA SENA":^30}')
print('-'*30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
    sleep(1)

print('-='*3, f'Sorteando {quantidade} jogos', '-='*3)
for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')
    sleep(1)
