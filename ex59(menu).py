
escolha = 0
print('-='*20)
print('MENU INTERATIVO')
print('-='*20)
num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))
while escolha != 5:
    print ('[1] SOMAR')
    print ('[2] MULTIPLICAR')
    print ('[3] MAIOR')
    print ('[4] NOVOS NUMEROS')
    print ('[5] SAIR DO PROGRAMA')
    escolha = int(input('Qual sua escolha: '))
    if escolha == 1:
        print ('A soma dos números é {}'.format(num1 + num2))
    elif escolha == 2:
        print ('A multiplicação dos números é {}'.format(num1 * num2))
    elif escolha == 3:
        if num1 > num2:
            print('O maior número é {}'.format(num1))
        elif num1 < num2:
            print('O maior número é {}'.format(num2))
        else:
            print('Os números são iguais')
    elif escolha == 4:
        print ('Digite dois novos números')
        num1 = int(input('Digite um numero inteiro: '))
        num2 = int(input('Digite outro numero inteiro: '))
    elif escolha == 5:
        print ('Você decidiu sair do menu')
    else:
        print ('Escolha invalida, digite entre 1 e 5')
print ('Fim do Menu')

