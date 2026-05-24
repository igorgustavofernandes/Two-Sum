matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = par = segundacoluna = maior_segunda_linha= 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para a linha {l} da coluna {c}: '))
        soma = soma + matriz[l][c]
        if matriz[l][c] % 2 == 0:
            par = par + matriz[l][c]
        if c == 1:
            segundacoluna += matriz[l][c]
    for c in range(0, 3):
        if c == 0 or matriz[1][c] > maior_segunda_linha:
            maior_segunda_linha = matriz[1][c]
maior_segunda_linha = max(matriz[1])
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma total é {soma}')
print(f'A soma dos números da segunda coluna é {segundacoluna}')
print(f'A soma dos números pares é {par}')
print(f'O maior número da segunda linha é {maior_segunda_linha}')
