km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias foram percorridos? '))
aluguel = dias * 60 + km * 0.15
print ('Calculando o valor a partir dos dias e dos kms percorridos, a sua conta a pagar do aluguel do carro é de {:.2f} reais'.format(aluguel))