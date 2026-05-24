numbers = list()
maior = menor = 0

for c in range(0, 5):
    numbers.append(int(input(f'Digite um valor para a posição {c}º: ')))
    if c == 0:
        maior = menor = numbers[c]
    else:
        if numbers[c] > maior:
            maior = numbers[c]
        elif numbers[c] < menor:
            menor = numbers[c]
print(f'Você digitou os valores {numbers}')
for i, v in enumerate(numbers):
    if v == maior:
        print(f'O menor número foi {menor} e a sua posição é {numbers.index(menor)}.', end=' ')
        print()
for i, v in enumerate(numbers):
    if v == menor:
        print(f'O maior número foi {maior} e a sua posição é {numbers.index(maior)}.', end=' ')
        print()