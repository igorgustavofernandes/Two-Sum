n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print ('O primeiro valor ({}) é maior que o segundo ({})'.format(n1, n2))
elif n1 < n2:
    print ('O segundo valor ({}) é maior que o primeiro ({})'.format(n2, n1))
else:
    print ('Nenhum valor é maior, ambos são iguais')