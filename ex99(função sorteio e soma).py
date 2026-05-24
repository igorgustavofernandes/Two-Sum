from time import sleep
from random import randint

def sorteio(lista):
    print('Sorteando 5 números: ', end='')
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('Fim')

def somapar(lista):
    soma = 0
    print('Somando números pares da lista sorteada....')
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos valores pares da lista sorteada é {soma}')


numeros = list()
sorteio(numeros)
somapar(numeros)