a = 0
b = 1
res = int(input('Digite em qual número deseja começar: '))
elem = int(input('Digite quantos elementos deseja mostrar: '))
print (a, b, end='->')
while res < elem:
    res += 1
    c = a + b
    print(c, end='->')
    a = b
    b = c
