print('-'*30)
print('Banco Bradesco')
print('-'*30)
valor = int(input('Digite um valor: '))
total = valor
cedula = 50
totced = 0
while True:
    if total >= cedula:
        totced -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedula de R${cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
    if total == 0:
        break



