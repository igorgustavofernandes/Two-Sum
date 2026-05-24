num = int(input('Digite um valor inteiro: '))
print ('''OPÇÕES DE BASE PARA CONVERSÃO:
[1] BINÁRIO
[2) OCTAL
[3] HEXADECIMAL''')
escolha = int(input('Escolha uma das opções acima para realizar a conversão: '))
if escolha == 1:
    print ('A conversão do número {} digitado anteriormente, em binário é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print ('A conversão do número {} digitado anteriormente, em octal é {}'.format(num, oct(num)[2:]))
else:
    print ('A conversaõ do número {} digitado anteriormente, em hexa é {}'.format(num, hex(num)[2:]))