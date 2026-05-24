numeros = [[], []]
valor = 0
for c in range(1, 8):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print('Listas de par e impar geradas')
desejo = str(input('Qual lista você deseja ver? (P/I): ')).strip().upper()
if desejo == 'P':
    print(f'A lista de números pares é {numeros[0]}')
elif desejo == 'I':
    print(f'A lista de números impares é {numeros[1]}')