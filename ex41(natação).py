from datetime import date
print('-='*20)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-='*20)
nome = str(input('Digite o nome do(a) atleta: ')).strip()
nascimento = int(input('Digite o nascimento do(a) {}: '.format(nome)))
idade = date.today().year - nascimento
if idade <= 9:
    print('Atleta MIRIM(até 9 anos)')
elif idade <= 14:
    print('Atleta INFANTIL(até 14 anos)')
elif idade <= 19:
    print('Atleta JUNIOR(até 19 anos)')
elif idade <= 20:
    print('Atleta SENIOR(até 20 anos)')
else:
    print('Atleta MASTER(acima de 20 anos)')