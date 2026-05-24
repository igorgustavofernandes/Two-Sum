casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu sálario: R$'))
anos = int(input('Digite quantos anos deseja pagar: '))
meses = anos*12
prestacao = casa/meses
if prestacao < salario*0.75:
    print('Seu empréstimo foi aprovado!')
    print('Sua prestação será de R${:.2f}'.format(prestacao))
elif prestacao > salario*0.75:
    print('Infelizmente seu emprestimo não pode ser aprovado!')
    print('A prestação de {:.2f}R$ ultrapassa 30% do seu sálario'.format(prestacao, salario))