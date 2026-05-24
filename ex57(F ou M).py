sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print ('Digite seu sexo de forma válida, com [M/F] ')
print('Concluído')