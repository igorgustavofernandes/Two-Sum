from datetime import date
maioridade = 0
menoridade = 0
for c in range(1, 7+1):
    data = int(input('Digite a {}º data de nascimento: '.format(c)))
    idade = date.today().year - data
    if idade >= 18:
        maioridade += 1
    elif idade < 18:
        menoridade += 1
print ('{} São menor de idade'.format(menoridade))
print ('{} São maior de idade'.format(maioridade))