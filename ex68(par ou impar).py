from random import randint
from time import sleep
total = 0
while True:
    escolha = str(input('IMPAR ou PAR? ')).strip().upper()
    if escolha == 'PAR':
        print('Então eu sou IMPAR')
    elif escolha == 'IMPAR':
        print('Então eu sou PAR')
    else:
        print('Escolha invalida')
    escolhido = randint(0, 10)
    sleep(1)
    print('IMPAR')
    sleep(1)
    print('OU')
    sleep(1)
    print('PAR')
    sleep(1)
    meunumero = int(input('Quantos você jogou? '))
    if escolha == 'PAR':
        if (meunumero + escolhido) % 2 == 0:
            print(f'Você venceu, eu joguei {escolhido} e você {meunumero}. Somando ambos dá {meunumero+escolhido} = PAR')
            total += 1
        elif (meunumero + escolhido) % 2 != 0:
            print(f'Você perdeu, eu joguei {escolhido} e você {meunumero}. Somando ambos dá {meunumero+escolhido} = IMPAR')
            break
    elif escolha == 'IMPAR':
        if (meunumero + escolhido) % 2 == 0:
            print(f'Você perdeu, eu joguei {escolhido} e você {meunumero}. Somando ambos dá {meunumero + escolhido} = PAR')
            break
        elif (meunumero + escolhido) % 2 != 0:
            print(f'Você venceu, eu joguei {escolhido} e você {meunumero}. Somando ambos dá {meunumero + escolhido} = IMPAR')
            total += 1
print(f'Você venceu um total de {total} vez(es)')


