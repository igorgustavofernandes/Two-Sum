velocidade = float(input('Qual a velocidade do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print ('\033[31mVoce foi multado!')
    print ('Sua multa é de {}R$'.format(multa))
else:
    print ('\033[35mVocê está na velocidade permitida')
