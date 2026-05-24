nome = str(input('Digite seu nome completo: ')).strip()
print ('Seu nome em letras maiúsculas é {}: '.format(nome.upper()))
print ('Seu nome em letras mínusculas é {}: '.format(nome.lower()))
print ('Seu nome tem esse número de letras: {} '.format(len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

