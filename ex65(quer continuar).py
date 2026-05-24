maior = 0
menor = 0
media = 0
total = 0
soma = 0
r = 0
num = 0
desejo = 0
while desejo != 'N':
    num = int(input('Digite um valor inteiro: '))
    total += 1
    soma += num
    media = soma / total
    if total == 1:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    desejo = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('O maior número digitado foi {}, o menor {} e a média de todos os números é {:.2F}'.format(maior,menor,media))
