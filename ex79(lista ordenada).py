numbers = []
while True:
    number = int(input('Digite um valor inteiro: '))
    if number not in numbers:
        numbers.append(number)
        print('Valor inserido foi adicionado na lista.')
    else:
        print('Esse número já existe, portanto, não será adicionado')
    ask = str(input('Quer continuar? [S/n]: '))
    if ask in 'Nn':
        break
print(f'A lista ficou assim {numbers}')
question = str(input('Quer ordenar em ordem crescente ou decrescente? [C/D]: ')).strip().upper()
if question == 'D':
    numbers.sort(reverse=True)
    print(f'Ordem crescente: {numbers}')
elif question == 'C':
    numbers.sort()
    print(f'A lista ordenada é {numbers}')