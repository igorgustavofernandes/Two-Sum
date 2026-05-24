from random import randint
from time import sleep
print('-='*20)
print('MINI GAME: JOKENPO')
print('-='*20)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
opcao = randint(0, 2)
jogada_maquina = lista[opcao]
sleep(1)
print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura...')
sleep(1)
jogada_minha = str(input('Qual você jogou? ')).strip().upper()
print('Eu joguei {}'.format(jogada_maquina))
sleep(1)
if jogada_maquina == jogada_minha:
    print ('Empatamos.')
elif jogada_maquina == "TESOURA" and jogada_minha == "PEDRA":
    print ('Você venceu! PEDRA quebra TESOURA')
elif jogada_maquina == "TESOURA" and jogada_minha == "PAPEL":
    print ('Eu venci! TESOURA corta PAPEL')
elif jogada_maquina == "PEDRA" and jogada_minha == "TESOURA":
    print ('Eu venci! PEDRA quebra TESOURA')
elif jogada_maquina == "PEDRA" and jogada_minha == "PAPEL":
    print ('Você venceu! PAPEL embrulha PEDRA')
elif jogada_maquina == "PAPEL" and jogada_minha == "PEDRA":
    print ('Eu venci! PAPEL embrulha PEDRA')
elif jogada_maquina == "PAPEL" and jogada_minha == "TESOURA":
    print ('Você venceu! TESOURA corta PAPEL')
else:
    print('Escolha (PAPEL, PEDRA OU TESOURA)!')