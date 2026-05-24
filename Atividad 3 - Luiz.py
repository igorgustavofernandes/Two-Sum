data = str(input('Digite a data do seu nascimento(**/**/****): '))
data = data.split('/')
dia = int(data[0])
if dia > 31 or dia < 1:
    print('Dia inválido')
mes = int(data[1])
if mes == 1:
    mes = 'Janeiro'
elif mes == 2:
    mes = 'Fevereiro'
elif mes == 3:
    mes = 'Março'
elif mes == 4:
    mes = 'Abril'
elif mes == 5:
    mes = 'Maio'
elif mes == 6:
    mes = 'Junho'
elif mes == 7:
    mes = 'Julho'
elif mes == 8:
    mes = 'Agosto'
elif mes == 9:
    mes = 'Setembro'
elif mes == 10:
    mes = 'Outubro'
elif mes == 11:
    mes = 'Novembro'
elif mes == 12:
    mes = 'Dezembro'
else:
    print('Mês inválido')
ano = int(data[2])
if ano < 0:
    print('Ano inválido')
else:
    print(f'Você nasceu no dia {dia} do mês {mes} do ano {ano}')
idade = 2026 - ano
print(f'Você tem {idade} anos.')