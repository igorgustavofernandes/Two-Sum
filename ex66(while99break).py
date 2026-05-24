n = c = s = 0
while True:
    n = int(input('Digite um valor inteiro (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou o total de {c} e a soma entre eles é de {s}')