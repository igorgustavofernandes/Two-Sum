salario = float(input('Digite o seu salario: '))
if salario <= 1250:
    aumento = (salario * 15) / 100 + salario
    print('Seu sálario apartir de agora passará a valer \033[1;32m{:.2f}\033[mR$ com o \033[4maumento de 15%\033[m'.format(aumento))
else:
    aumento =(salario * 10) / 100 + salario
print('Seu salário apartir de agora passará a ser \033[1;32m{:.2f}\033[mR$ com o \033[4maumento de 10%\033[m'.format(aumento))
