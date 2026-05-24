from datetime import date
nome = str(input('Digite seu nome: '))
nascimento = float(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
if idade > 18:
    print('Seu tempo de se alistar já passou à {:.0F} anos, caro {}.'.format(18 - idade, nome))
elif idade < 18 and idade > 17:
    print('Ainda falta {:.0F} ano para o seu alistamento, caro {}'.format(18 - idade, nome))
elif idade <18 and idade < 17:
    print('Ainda falta {:.0F} anos para o seu alistamento, caro {}'.format(18 - idade, nome))
elif idade == 18:
    print('Está na hora de se alistar, caro {}'.format(nome))