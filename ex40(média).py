print('-='*20)
print('INSTITUTO ESTADUAL DE EDUCAÇÃO "DR. CAETANO MUNHOZ DA ROCHA"')
print('Matéria de: Química')
print('-='*20)
n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
media = (n1 + n2) / 2
if media >= 7:
    print('Aprovado. sua média foi {}. Parabéns!!!'.format(media))
elif media >= 5:
    print('Recuperação. sua média foi {}. Estude mais!!!'.format(media))
else:
    print('Reprovado. sua média foi {}. Sinto muito!'.format(media))
