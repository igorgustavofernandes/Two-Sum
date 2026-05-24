from random import randint
from time import sleep
escolha_maquina= randint(0,10)
print ('-='*20)
print ('Jogo: IMPAR ou PAR')
print ('-='*20)

minha_escolha = str(input('IMPAR ou PAR? ')).upper()
if minha_escolha == 'PAR':
    print ('Então eu serei IMPAR')
else:
    print ('Então eu serei PAR')

meu_numero = int(input('Escolha um número de 0 a 10: '))
print ('Eu joguei {}'.format(escolha_maquina))
soma = meu_numero + escolha_maquina
print ("Verificando...")
sleep(3)
if soma % 2 == 0:
    print ('{} + {} = {} ou seja, deu PAR'.format(escolha_maquina, meu_numero, soma))
    if minha_escolha == 'PAR':
        print ('Você escolheu {}. Então você ganhou!'.format(minha_escolha))
    else:
        print ('Você escolheu {}. Então você perdeu!'.format(minha_escolha))
else:
    print ('{} + {} = {} ou seja, deu IMPAR'.format(escolha_maquina, meu_numero, soma))
    if minha_escolha == 'IMPAR':
        print ('Você escolheu {}. Então você ganhou!'.format(minha_escolha))
    else:
        print ('Você escolheu {}. Então você perdeu!'.format(minha_escolha))

