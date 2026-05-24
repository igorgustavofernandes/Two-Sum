from datetime import date
ano = int(input('Digite um ano qualquer (Digite 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year
    print ('Você está em {}'.format(ano))
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    if ano < date.today().year:
        print('\033[32mEsse \033[7mfoi\033[m \033[32mum ano BISSESTO')
    elif ano == date.today():
        print("\033[32mEsse \033[7mé\033[m \033[32mum ano BISSESTO\033[m")
    else:
        print('\033[32mEsse \033[7mvai ser\033[m \033[32mum ano BISSESTO\033[m')
else:
    if ano < date.today().year:
        print('\033[31mEsse \033[7mnão\033[m \033[31mfoi um ano BISSESTO\033[m')
    elif ano == date.today().year:
        print('\033[31mEsse \033[7mnão é\033[m \033[31mum ano BISSESTO\033[m')
    else:
        print('\033[31mEsse \033[7mnão vai ser\033[m \033[31mum ano BISSESTO\033[m')