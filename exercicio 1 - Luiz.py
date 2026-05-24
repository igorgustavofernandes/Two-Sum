lista = list()
for i in range(3):
    lista.append(int(input("Digite um valor: ")))
for i, l in enumerate(lista):
    print(f'O valor {l} está na posição {i}')