somaidade = 0
abaixodevinte = 0
homemmaisvelho = 0
nomemaisvelho = ''
for c in range(1, 4+1):
    nome = str(input('Digite o {}º nome: '.format(c)))
    idade = int(input('Digite a {}º idade: '.format(c)))
    sexo = str(input('Digite o {}º sexo (M - Masculino ou F - Feminino): '.format(c))).strip()
    somaidade += idade
    if sexo in 'Mm' and c == 1:
        homemmaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomemaisvelho = nome
    elif sexo in 'Fm' and idade < 20:
        abaixodevinte += 1
media = somaidade / 4
print('A média de  idade é {:.0F} anos'.format(media))
print('O homem mais velho é o {}.'.format(nomemaisvelho))
print('{} mulheres tem menos de 20 anos'.format(abaixodevinte))