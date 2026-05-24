number = int(input('Type a number: '))
if number % 2 == 0:
    print ('\033[1;45m{} is even\033[m'.format(number))
else:
    print('\033[1;46m{} is odd\033[m'.format(number))