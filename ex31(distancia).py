distance = int(input('Enter the distance of the trip: '))

if distance > 200:
    preco = distance * 0.45
    print ('Your trip will cost \033[4m{}$'.format(preco))
else:
    preco = distance * 0.50
    print ('Your trip will cost \033[4m{}$'.format(preco))


