for c in range(1,5+1):
    peso = (float(input('Fale o {}º peso: KG'.format(c))))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print ('O maior peso é {}KG e o menor é {}KG'.format(maior,menor))

