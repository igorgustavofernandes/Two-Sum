n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
lista = ['primeiro', 'segundo', 'terceiro' ]
menor = n1
ordem_menor = lista[0]
if n2 < n1 and n2 < n3:
    menor = n2
    ordem_menor = lista[1]
if n3 < n1 and n3 < n2:
    menor = n3
    ordem_menor = lista[2]
print ('O menor número digitado foi o \033[4m{}\033[m: \033[31m{}\033[m'.format(ordem_menor, menor))
maior = n1
ordem_maior = lista[0]
if n2 > n1 and n2 > n3:
    maior = n2
    ordem_maior = lista[1]
if n3 > n1 and n3 > n2:
    maior = n3
    ordem_maior = lista[2]
print ('O maior valor digitado foi o \033[4m{}\033[m: \033[34m{}\033[m'.format(ordem_maior, maior))