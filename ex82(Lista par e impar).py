lista = list()
lista_impar = list()
lista_par = list()
while True:
    num = int(input('Digite um valor para a lista: '))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    desejo = str(input('Quer continuar? [S/N] ')).strip().upper()
    if desejo == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {lista_par}')
print(f'A lista de números impares é {lista_impar}')