from math import hypot
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('Calculando a hipotenusa do cateto oposto e a hipotenusa do cateto adjacente chegamos no resultado de {:.4f}'.format(hipotenusa))