from random import randint
opcoes = ['CCAARA', 'COROA']
sorteio = randint(0,1)
caiu = opcoes[sorteio]
print ('-='*20)
print ('Jogo: CARA ou COROA')
print ('-='*20)
escolha = str(input('Escolha: CARA ou COROA: ').upper().strip())
if escolha == caiu:
    print ('Você ganhou! caiu {}'.format(caiu))
else:
    print ('Você perdeu! caiu {}'.format(caiu))
