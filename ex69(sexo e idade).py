total_homens = 0
demaior = 0
mulheres_abaixo_de_20 = 0
while True:
    escolha = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        total_homens += 1
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        demaior += 1
    if sexo == 'F' and idade < 20:
        mulheres_abaixo_de_20 += 1
    while escolha not in 'SN':
        escolha = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'O total de homens cadastrados foi {total_homens}')
print(f'O total de pessoas acima de 18 anos foi {demaior}')
print(f'O total de mulheres abaixo de 20 anos foi {mulheres_abaixo_de_20}')


