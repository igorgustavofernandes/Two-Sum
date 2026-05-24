s = 0
for c in range(1, 500+1):
    if c % 3 == 0:
        s = s + c
print('O total da soma dos números impares de 1 ao 500 é = {}'.format(s))