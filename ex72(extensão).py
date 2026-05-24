extensao = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = ''
while escolha != 'N':
    escolha = str(input('Deseja ver um número por extenso? (S/N): ')).strip().upper()[0]
    if escolha == 'S':
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20 :
            print(f'{numero} por extenso é {extensao[numero]}')
        else:
            print(f'Digite um número entre 0 e 20')
