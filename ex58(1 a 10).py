from random import randint
escolha_maquina = randint(1,11)
minha_escolha = 0
chances = 0
while minha_escolha != escolha_maquina:
    chances += 1
    minha_escolha = int(input('Digite um número de 1 a 10: '))
    if minha_escolha != escolha_maquina:
        print('Você errou!! tente novamente')
    elif minha_escolha == escolha_maquina:
        print('Você acertou!! Parabéns')
print ('Fim do jogo, você precisou de {} chances.'.format(chances))