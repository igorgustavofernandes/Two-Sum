print('-='*20)
print('Drible House: Artigos Esportivos.')
print('-='*20)
print('Tabela de produtos:')
print('Modelo Atual: 100R$')
print('Modelo Retro: 130R$')
print('Modelo Jogador: 150R$')
print('Manga Longa: 140R$')
atual = 100
retro = 130
jogador = 150
longa = 140
desejo = int(input('Digite o produto que você deseja pelo valor dele: R$ '))
if desejo == 100:
    print('Você deseja uma camisa modelo atual')
elif desejo == 130:
    print('Você deseja uma camisa modelo retro')
elif desejo == 150:
    print('Você deseja uma camisa modelo jogador')
elif desejo == 140:
    print('Você deseja uma camisa manga longa')
else:
    print('Escolha uma das opções disponiveis')
print('Formas de pagamento: ')
print('(1)Dinheiro/Check(10% de desconto)')
print('(2)Cartão à vista(5% de desconto)')
print('(3)Parcelado(Preço normal)')
print('(4)Parcelado 3x ou mais(20% de juros)')
forma = int(input('Qual seria a forma de pagamento? (1,2,3,4 ou 5): '))
if forma == 1:
    valor = desejo - (desejo * 0.10)
    print('No dinheiro ou check, com o desconto de 10% fica {:.0F}R$'.format(valor))
elif forma == 2:
    valor = desejo - (desejo * 0.05)
    print('À vista no cartão, com o desconto de 5% fica {}R$'.format(valor))
elif forma == 3:
    print ('No cartão, sem desconto fica pelo preço normal, {}R$'.format(desejo))
elif forma == 4:
    valor = desejo + (desejo * 0.20)
    print('Parcelado em 3 ou mais vezes, o valor com o juros de 20% fica {}R$'.format(valor))
else:
    print('Digite um valor válido (de 1 ao 5)')

