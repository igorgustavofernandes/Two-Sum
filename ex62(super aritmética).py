print('-='*20)
print('SUPER PROGRESSÃO ARITMÉTICA')
print('-='*20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10 # Começamos querendo os 10 primeiros

while mais != 0:
    total = total + mais # O total de termos que queremos ver até agora
    while cont <= total:
        print(f'{termo}', end=' → ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? (0 para sair): '))

print(f'Progressão finalizada com {total} termos mostrados.')