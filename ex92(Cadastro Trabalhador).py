from datetime import date
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade´'] = date.today().year - nascimento
dados['carteira'] = int(input('Carteira de Trabalho (0 não possuí): '))
if dados ['carteira'] != 0:
    dados['ano'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = 65
for k, v in dados.items():
    print(f'{k} tem o valor {v}')